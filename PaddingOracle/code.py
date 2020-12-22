from pwn import *
import pybase64

conn = remote('140.114.77.172', 8013)
cipherb64 = conn.recvlineS()
cipher = pybase64.b64decode(cipherb64)

# 32 to 126 are readable character

plaintext = list("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

mod_cipher = list(cipher)
print(cipher)
print(type(cipherb64))


for i in range(256):
    mod_cipher[len(mod_cipher)-1] = i
    try_cipher_enc = str(pybase64.b64encode(bytes(mod_cipher)))
    print(type(try_cipher_enc))
    conn.send(try_cipher_enc)
    conn.send('\n')
    s1 = conn.recvlineS()
    if (s1[0] == 'C'):
        print("found")
        break
print(mod_cipher)

'''
for i in range(63, -1, -1):
    for j in range(32, 127):
        plaintext[i] = chr(j)
        p = "".join(plaintext)
        p_enc = pybase64.b64encode(p.encode('ascii'))
        conn.send(p_enc)
        conn.send('\n')
        s1 = conn.recvlineS()
        if (s1[0] == 'C'):
            print("found")
            break
    if (j == 126):
        print("can't find")
print(plaintext)
'''

conn.close()
