from pwn import *
conn = remote('140.114.77.172', 8015)
s = conn.recvlineS()
print(s)
