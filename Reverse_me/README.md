# Reverse me
This project aims to learn Reversing Engineering with gdb.


Each executables request password.
We find the proper password using gdb.

## level1

## level2
```
(gdb) disassemble main
Dump of assembler code for function main:
   0x565562d0 <+0>:	push   %ebp
   0x565562d1 <+1>:	mov    %esp,%ebp
   0x565562d3 <+3>:	push   %ebx
=> 0x565562d4 <+4>:	sub    $0x54,%esp
   0x565562d7 <+7>:	call   0x565562dc <main+12>
   ...
   0x565562fe <+46>:	lea    -0x35(%ebp),%eax # -> Load address for input buffer
   0x56556301 <+49>:	lea    -0x42d2(%ebx),%ecx
   0x56556307 <+55>:	mov    %ecx,(%esp)
   0x5655630a <+58>:	mov    %eax,0x4(%esp)
   0x5655630e <+62>:	call   0x565560c0 <__isoc99_scanf@plt>
   ...
   0x5655632c <+92>:	movsbl -0x34(%ebp),%ecx # -> Load second byte of input (password[1]) from stack into ecx register
   0x56556330 <+96>:	mov    $0x30,%eax # -> Load 0x30 ('0' in ascii) to eax register
   0x56556335 <+101>:	cmp    %ecx,%eax
   0x56556337 <+103>:	je     0x56556345 <main+117> # -> Jump if ecx and eax are equal (password[1] must be '0')
   ...
```

## execute
```bash
cd Reverse_me
docker build -t ubuntu .
docker run -it -v ./submit:/home/ubuntu ubuntu /bin/bash
```
