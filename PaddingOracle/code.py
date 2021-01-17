from pwn import *
import pybase64

conn = remote('140.114.77.172', 8013)
cipherb64 = conn.recvlineS()
cipher = pybase64.b64decode(cipherb64)

# 32 to 126 are readable character

plaintext = list("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

mod_cipher = list(cipher)
print(len(mod_cipher))
#print(type(mod_cipher))

text = [0] * 64

# 8th block
for block in range(7):
    prev_block_idx = 8*(7-block) - 1
    for rounds in range(8):
        mod_cipher = list(cipher)
        if (rounds == 0):
            for i in range(256):
                mod_cipher[prev_block_idx] = i
                try_cipher_enc = pybase64.b64encode(bytes(mod_cipher)).decode('utf-8')
            #    print(try_cipher_enc)
                conn.send(try_cipher_enc)
            #    print("send text")
                conn.send('\n')
            #    print("send next line")
                s1 = conn.recvlineS()
            #    print(s1[0])
            #    print("recive")
                if (s1[2] == 'C'):
                    print("found i = " + str(i))
                    break
            print(mod_cipher)

            # last byte is i xor 1
            text[prev_block_idx+8] = i ^ 1
        else:
            for i in range(rounds):
                index = prev_block_idx - rounds
                for j in range(256):
                    if (j ^ text[index+8]) == 2:
                        mod_cipher[index] = j
                        break
            for j in range(256):
                mod_cipher[index] = j
                try_cipher_enc = pybase64.b64encode(bytes(mod_cipher)).decode('utf-8')
                conn.send(try_cipher_enc)
                conn.send('\n')
                s1 = conn.recvlineS()
                if (s1[2] == 'C'):
                    print("found j = " + str(j))
                    break
            print(mod_cipher)
            text[index+8] = j ^ (rounds + 1)

mod_cipher = list(cipher)
new = [0]*64
print(text)
print(len(mod_cipher))

for i in range(64):
    if (i < 7):
        continue
    else:
        new[i] = text[i] ^ mod_cipher[i - 8]

print(new)

print(pybase64.b64decode(bytes(new)).decode('utf-8'))




'''
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
