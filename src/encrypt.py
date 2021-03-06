from cryptography.fernet import Fernet
import pyqrcode

#generate the encryption key 
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)

#load key from directory
def load_key():
    return open("secret.key","rb").read()

#encrypt the message
def encrypt_message(message):
    generate_key()
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    big_code = pyqrcode.create(encrypted_message, error='L', version=27, mode='binary')
    big_code.png('new.png', scale=4, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xcc])
    big_code.show()

