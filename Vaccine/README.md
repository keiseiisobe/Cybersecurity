# Vaccine 💉
A program that performs an SQL injection.

## execute
```bash
# for DVWA
shell % ./vaccine http://localhost:4280/vulnerabilities/sqli/

# for sqlite-injection
shell % ./vaccine -X POST http://localhost:8000

shell % ./vaccine -h
usage: vaccine [-h] [-o OUT] [-X {GET,POST}] URL

A program that performs a SQL injection.

positional arguments:
  URL                   The URL to perform the SQL injection on.

options:
  -h, --help            show this help message and exit
  -o, --out OUT         The output file to save the results to. (default="output.txt")
  -X, --request {GET,POST}
                        The HTTP request method to use (GET or POST). (defalut="GET")
```

## set test environments
```bash
shell % make help
Command List:

dvwa:         run dvwa app # -> test for MySQL based valunerable web app
dvwa-down:    stop dvwa app
sqlitei:      run sqlite-injection app # -> test for SQLite based valunerable web app
sqlitei-down: stop sqlite-injection app
```

## reference
* https://github.com/digininja/DVWA
* https://gitlab.cylab.be/cylab/play/sqlite-injection