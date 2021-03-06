from cryptography.fernet import Fernet

#generate the encryption key 
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)

#load key from directory
def load_key():
    return open("secret.key","rb").read()

#encrypt the message
def encrypt_message():
message = "message I want to encrypt".encode()
f = Fernet(key)
encrypted_message = f.encrypt(message)


