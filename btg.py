import hashlib

crypt=hashlib.md5()
crypt.update(b'Estou sendo criptografado')
print(crypt.hexdigest())