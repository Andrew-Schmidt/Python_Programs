#!/bin/python3
from cryptography.fernet import Fernet
key_write = Fernet.generate_key()
key = open("key.txt", "wb")
key.write(key_write)
key.close
crypter = Fernet(key)
pw = crypter.encrypt(b'password')
decryptString = crypter.decrypt(pw)
print(str(pw, 'utf8'))
print(str(decryptString, 'utf8'))
