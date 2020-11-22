from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
from Cryptodome import Random
from base64 import b64encode, b64decode

ks = AES.key_size[0] # 16 bytes
key = Random.get_random_bytes(ks)
iv = Random.get_random_bytes(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
with open('flag','rb') as f:
	flag = f.read().strip()
flag = Padding.pad(flag, ks, style='pkcs7')
flag_enc = b64encode(iv + cipher.encrypt(flag)).decode('ASCII')
print(flag_enc)
while True:
	query = bytes(input('>>'), 'ASCII')
	query = b64decode(query)
	cipher = AES.new(key, AES.MODE_CBC, iv=query[:16])
	flag_dec = cipher.decrypt(query[16:])
	try:
		Padding.unpad(flag_dec, ks, style='pkcs7')
		print('Correct Padding!')
	except ValueError:
		print('Error Padding!')
