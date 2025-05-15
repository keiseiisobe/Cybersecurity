# ft_opt 🗝️
A script that generates a new one time password every time it is requested.

## execute
```bash
# store encoded secure key in new file.
shell % cat key.hex 
0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF%

shell % ./ft_opt -g key.hex 
Key was successfully saved in ft_opt.key.
QR code was successfully saved in ft_opt.png.

#  generates a new temporary password based on the key given as argument.
shell % ./ft_opt -k ft_opt.key 
218357
```

## help
```bash
shell % ./ft_opt -h
usage: Stores an initial password, and generates a new one time password every time it is requested

optional arguments:
  -h, --help            show this help message and exit
  -g GENERATE, --generate GENERATE
  -k KEY, --key KEY
```

## reference
* https://datatracker.ietf.org/doc/html/rfc4226 (HOTP)
* https://datatracker.ietf.org/doc/html/rfc6238 (TOTP)
* https://datatracker.ietf.org/doc/html/rfc2104 (HMAC)
* https://datatracker.ietf.org/doc/html/rfc6234 (SHA)
