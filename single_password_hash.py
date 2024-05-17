import hashlib

Password = "Welcome12345"
hash = hashlib.sha256(Password.encode('utf-8'))
print(hash.hexdigest())
