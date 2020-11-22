print("`conn.recvlineS()` receives the next line! Let's see how to send message to the server. Read the next line for the command." )
print("conn.sendline('OK') #send OK folowing by a newline")
x = input()
while True:
	if x == 'OK':
		print('You can receive all remaining messages by: `conn.recvallS()`')
		break
	else:
		x = input("Send 'OK' use the command: `conn.sendline('OK')")

print("I make this tutorial since I hear somebody complain that he/she just doesn't know WTF is NC. But, this stuff can be easily found on the Internet and I HAD LEFT WHAT TO DO WHILE FACING PROBLEMS IN THE MAIN PAGE OF THE CTF PLATFORM(http://140.114.77.172:8000/) 2 WEEKS AGO. ")
print("flag{XXXXXXXXXXXXXXXXXXXXXX}")
