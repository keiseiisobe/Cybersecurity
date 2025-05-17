# ft_onion 🧅
A hidden service that is accessible from Tor network.


See https://community.torproject.org/onion-services/ to understand hidden services.


<img src="https://community.torproject.org/static/images/onion-services/overview/onion-service-09.png" width="500" height="500"/>

## execute
```bash
# if you don't have SSH key
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa

cp ~/.ssh/id_rsa.pub ~/ft_onion/nginx/secrets/authorized_keys
docker compose up
```

```bash
# if you want to connect remote server
ssh -i ~/.ssh/id_rsa -p 4242 sshuser@localhost
```

## How to see your websites on Tor browser
1. install [Tor browser](https://www.torproject.org/)
2. ```cat ~/ft_onion/tor/data/hostname | pbcopy # you can get onion address.```
3. paste it to the Tor browser
