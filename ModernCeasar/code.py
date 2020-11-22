f = open("cipher.txt", "r")
cipher = f.read()
cipher = cipher.rstrip('\n')
print(cipher)

import pybase64

new_c = " "

# base64 decode -> ceasar cipher
message = pybase64.b64decode(cipher)

new_message = ""
for c in message:
    new_c = chr((ord(c) + 19) % 128)
    new_message = new_message + new_c

#print(message[0])
print(new_message)

print("done")
