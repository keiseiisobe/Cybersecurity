# Stockholm 💸
A program that is harmless ransomware.

## General Information
This program only work in the "infection" folder in the user's home directory.

This program only act on following file extensions that have been affected by Wannacry.

(see https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/)

> .123, .jpeg , .rb , .602 , .jpg , .rtf , .doc , .js , .sch , .3dm , .jsp , .sh , .3ds , .key , .sldm , .3g2 , .lay , .sldm , .3gp , .lay6 , .sldx , .7z , .ldf , .slk , .accdb , .m3u , .sln , .aes , .m4u , .snt , .ai , .max , .sql , .ARC , .mdb , .sqlite3 , .asc , .mdf , .sqlitedb , .asf , .mid , .stc , .asm , .mkv , .std , .asp , .mml , .sti , .avi , .mov , .stw , .backup , .mp3 , .suo , .bak , .mp4 , .svg , .bat , .mpeg , .swf , .bmp , .mpg , .sxc , .brd , .msg , .sxd , .bz2 , .myd , .sxi , .c , .myi , .sxm , .cgm , .nef , .sxw , .class , .odb , .tar , .cmd , .odg , .tbk , .cpp , .odp , .tgz , .crt , .ods , .tif , .cs , .odt , .tiff , .csr , .onetoc2 , .txt , .csv , .ost , .uop , .db , .otg , .uot , .dbf , .otp , .vb , .dch , .ots , .vbs , .der” , .ott , .vcd , .dif , .p12 , .vdi , .dip , .PAQ , .vmdk , .djvu , .pas , .vmx , .docb , .pdf , .vob , .docm , .pem , .vsd , .docx , .pfx , .vsdx , .dot , .php , .wav , .dotm , .pl , .wb2 , .dotx , .png , .wk1 , .dwg , .pot , .wks , .edb , .potm , .wma , .eml , .potx , .wmv , .fla , .ppam , .xlc , .flv , .pps , .xlm , .frm , .ppsm , .xls , .gif , .ppsx , .xlsb , .gpg , .ppt , .xlsm , .gz , .pptm , .xlsx , .h , .pptx , .xlt , .hwp , .ps1 , .xltm , .ibd , .psd , .xltx , .iso , .pst , .xlw , .jar , .rar , .zip , .java , .raw

## execute

```bash
# on your host machine

# Just create container
shell % make run # or make

# Just build image
shell % make build

# Do both
shell % make all
```

```bash
# on your docker container

# encrypt files in infection folder
stockholm@424242:~$ ./stockholm

# decrypt files encrypted
stockholm@424242:~$ ./stockholm -r [key] # key is created in current directory when you encrypt files.
```

## Hamlet encryption and decryption

```bash
stockholm@424242:~$ cat infection/hamlet.txt | head 
BERNARDO
Who's there?
FRANCISCO
Nay, answer me: stand, and unfold yourself.
BERNARDO
Long live the king!
FRANCISCO
Bernardo?
BERNARDO
He.

stockholm@424242:~$ ./stockholm 
Key saved at ./key
Encrypting hamlet.txt...
Done.
Renamed hamlet.txt to hamlet.txt.ft
...

stockholm@424242:~$ cat infection/hamlet.txt.ft
gAAAAABoK0mwvRCvaavdE8ycbmlhztbKi0i6tr-5CfbEJY1XxyQ-yViW9FN22SV.....

stockholm@424242:~$ ./stockholm -r [key value]
Decrypting hamlet.txt.ft...
Done.
Renamed hamlet.txt.ft to hamlet.txt

stockholm@424242:~$ cat infection/hamlet.txt | head 
BERNARDO
Who's there?
FRANCISCO
Nay, answer me: stand, and unfold yourself.
BERNARDO
Long live the king!
FRANCISCO
Bernardo?
BERNARDO
He.
```


## help

```bash
stockholm@424242:~$ ./stockholm -h
usage: stockholm [-h] [-v] [-r REVERSE_KEY] [-s]

execute a harmless ransomware

options:
  -h, --help            show this help message and exit
  -v, --version         show the version of the script
  -r, --reverse REVERSE_KEY
                        reverse the encryption
  -s, --silent          run in silent mode

```