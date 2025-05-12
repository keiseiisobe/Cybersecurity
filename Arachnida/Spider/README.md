# Spider 🕷️
A script that extract all the images from a website recursively.

## execute
```bash
./spider [-rlp] URL
```

## extensions
Only follwing extensions are permitted.

* .jpg/jpeg
* .png
* .gif
* .bmp

## help
```bash
shell % ./spider -h
usage: Extract the images from a website.

positional arguments:
  URL

optional arguments:
  -h, --help            show this help message and exit
  -r, --recursive       recursively downloads the images in a URL
  -l LEVEL, --level LEVEL
                        indicates the maximum depth level of the recursive download
  -p PATH, --path PATH  indicates the path where the downloaded files will be saved
```
