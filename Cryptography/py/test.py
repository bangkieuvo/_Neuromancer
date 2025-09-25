from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Sinh cặp khóa RSA (2048 bit an toàn hơn)
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

# Tạo cipher dùng PKCS1_OAEP (padding an toàn)
cipher_rsa = PKCS1_OAEP.new(public_key)

# Mã hóa
message = b"Hello world!"
ciphertext = cipher_rsa.encrypt(message)
print("Ciphertext:", ciphertext)

# Giải mã
decipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = decipher_rsa.decrypt(ciphertext)
print("Plaintext:", plaintext)
