from pwn import *
import math

conn = remote('140.114.77.172', 8011)

for i in range(10000):
    S = conn.recvlineS()
    conn.send("0 0 0\n")

S1 = conn.recvlineS()
print(S1)

conn.close()
