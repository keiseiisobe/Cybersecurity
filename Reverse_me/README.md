# Reverse me

## execute
```bash
cd Reverse_me
docker build -t retdec - < Dockerfile
docker run -it -v ./submit:/home/retdec retdec /bin/bash
```