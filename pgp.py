#!usr/bin/python
# encoding:utf-8
import base64
import hashlib
import re
import os
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
 
"""
Note about PBEWithMD5AndDES in java crypto library:
Encrypt:
  Generate a salt (random): 8 bytes
  <start derived key generation>
  Append salt to the password
  MD5 Hash it, and hash the result, hash the result ... 1000 times
  MD5 always gives us a 16 byte hash
  Final result: first 8 bytes is the "key" and the next is the "initialization vector"
  (there is something about the first 8 bytes needing to be of odd paraity, therefore
  the least significant bit needs to be changed to 1 if required. We don't do it,
  maybe the python crypto library does it for us)
  <end derived key generation>
  Pad the input string with 1-8 bytes (note: not 0-7, so we always have padding)
    so that the result is a multiple of 8 bytes. Padding byte value is same as number of
    bytes being padded, eg, \x07 if 7 bytes need to be padded.
  Use the key and iv to encrypt the input string, using DES with CBC mode.
  Prepend the encrypted value with the salt (needed for decrypting since it is random)
  Base64 encode it -> this is your result
Decrypt:
  Base64 decode the input message
  Extract the salt (first 8 bytes). The rest is the encoded text.
  Use derived key generation as in Encrypt above to get the key and iv
  Decrypt the encoded text using key and iv
  Remove padding -> this is your result
"""

def main():
         rsa = RSA_encryto () # Создать объект сущности rsa
         commuicate_key = "helloworld" # Создать ключ сеанса
         msg = input ("msg:") # читать сообщения
         ec_msg = encrypt (msg, commuicate_key) # Зашифровать сообщение msg
 
         # 1. Экспорт ключа RSA на ПК
    ec_private_key = rsa.export_encypted_private_key()
         print ("ключ RSA после шифрования:" + str (ec_private_key))
 
         # 2. RSA зашифрованный сеансовый ключ
    publickey = rsa.export_public_key()
    rsakey = RSA.importKey(publickey)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(commuicate_key.encode(encoding='utf-8')))
#    cipher_text = cipher.encrypt(commuicate_key)
         print («Содержимое зашифрованного файла:« + str (ec_msg) + », ключ зашифрованного сеанса:« + str (cipher_text))
 
         # 3. Расшифровать закрытый ключ RSA
         пароль = ввод ("пароль:")
    rsa_privatekey = decrypt(ec_private_key, password)
 
         # 4. Расшифровать ключ сессии
         rsa_key = RSA.importKey (rsa_privatekey) # Импортировать закрытый ключ чтения
         cipher = Cipher_pkcs1_v1_5.new (rsa_key) # Создать объект
    commuicatekey = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")
#    commuicatekey = cipher.decrypt(cipher_text, "ERROR")
 
         # 5. Расшифровывать сообщения
    de_msg = decrypt(ec_msg, str(commuicatekey, encoding='utf-8'))
    print("msg:" + str(de_msg, encoding='utf-8'))
 
 
if __name__ == "__main__":
    main()




 
# Используйте пароль и соль для создания симметричного ключа и вектора инициализации
def get_derived_key(password, salt, count):
    key = str(password)+ str(salt)
    for i in range(count):
        m = hashlib.md5(str(key).encode('utf-8'))
        key = m.digest()
    return (key[:8], key[8:])
 
 # DES-CBC расшифровывать
def decrypt(msg, password):
    msg_bytes = base64.b64decode(msg)
    salt = msg_bytes[:8]
    enc_text = msg_bytes[8:]
    (dk, iv) = get_derived_key(password, salt, 1000)
 
    crypter = DES.new(dk, DES.MODE_CBC, iv)
    text = crypter.decrypt(enc_text)
    # remove the padding at the end, if any
    return re.split(rb'[\x01-\x08]',text)[0]
   #return re.sub(r'[\x01-\x08]', '', text.decode())
 
 
 
 # DES-CBC шифрование
def encrypt(msg, password):
    salt = os.urandom(8)
    pad_num = 8 - (len(msg) % 8)
    for i in range(pad_num):
        msg += chr(pad_num)
    (dk, iv) = get_derived_key(password, salt, 1000)
 
    crypter = DES.new(dk, DES.MODE_CBC, iv)
    enc_text = crypter.encrypt(msg.encode(encoding='utf-8'))
    return base64.b64encode(salt + enc_text)
 
 
 # Используется для расшифровки симметричного сеансового ключа
class RSA_encryto:
    def __init__(self):
        rsa = RSA.generate(1024, Random.new().read)
        private = rsa.exportKey()
        public_key = rsa.publickey().exportKey()
        self.__private_key = private
        self.public_key = public_key
        self.__rsa = rsa
 
    def export_public_key(self):
        return self.public_key
 
 
    def export_encypted_private_key(self):
        salt = os.urandom(8)
 
        private = self.__private_key
 
        pad_num = 8 - (len(private) % 8)
        for i in range(pad_num):
            private += chr(pad_num).encode(encoding='utf-8')
                 пароль = ввод ("пароль:")
        (dk, iv) = get_derived_key(password, salt, 1000)
 
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        enc_text = crypter.encrypt(private)
        return base64.b64encode(salt + enc_text)
 
 
 
