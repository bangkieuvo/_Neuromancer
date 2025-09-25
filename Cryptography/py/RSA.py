class RSA():
	def genKey(self,bit = 15):
		from Crypto.Util import number
		from numberTheory import GCD,modularInverse
		p = number.getPrime(bit//2)
		q = number.getPrime(bit//2)
		n = p*q
		phi = (p-1)*(q-1)
		e = number.getPrime(7)
		while GCD(e,phi)!=1:
			e = number.getPrime(7)
		d = modularInverse(e,phi)
		return (e,n), (d,n)
	def encrypt(self,plaintext,key):
		if type(plaintext).__name__ != "bytes":
			plaintext = plaintext.encode()
		cipher = b''
		for num in plaintext:
			num = (num**key[0])%key[1]
			cipher = cipher + num.to_bytes(2,'big')
		return cipher
	def decrypt(self,ciphertext,key):
		if type(ciphertext).__name__ != "bytes":
			print(type(ciphertext))
			ciphertext = ciphertext.encode()
		plaintext = b''
		for i in range(0, len(ciphertext), 2):
		    c = int.from_bytes(ciphertext[i:i+2], 'big')  # đọc lại số nguyên
		    m = pow(c, key[0], key[1])        # RSA decrypt
		    plaintext += bytes([m]) 
		return plaintext  
# rsa = RSA()
# key = rsa.genKey()
# publicKey = key[0]
# privateKey = key[1]
# print(publicKey)
# s = 'Hello world!'
# s = s.encode()
# print(s)
# cipher = b''
# for num in s:
# 	num = (num**publicKey[0])%publicKey[1]
# 	cipher = cipher + num.to_bytes(2,'big')
# 	print(num)
# print("cipher: ",cipher)
# plaintext = b''
# for i in range(0, len(cipher), 2):
#     c = int.from_bytes(cipher[i:i+2], 'big')  # đọc lại số nguyên
#     m = pow(c, privateKey[0], privateKey[1])        # RSA decrypt
#     plaintext += bytes([m])    
# print("plaintext: ",plaintext)
		
# 		