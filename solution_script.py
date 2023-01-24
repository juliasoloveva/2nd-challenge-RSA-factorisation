from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Read the private key from a file
with open("private_key.pem", "rb") as key_file:
    private_key = RSA.import_key(key_file.read())

# Read the encrypted message from a file
with open("ciphertext.bin", "rb") as ciphertext_file:
    ciphertext = ciphertext_file.read()

# Decrypt the message using the private key
cipher = PKCS1_OAEP.new(private_key)
plaintext = cipher.decrypt(ciphertext)

# Check if the plaintext starts with "flag"
if plaintext.startswith(b"flag"):
    print("Flag:", plaintext.decode())
else:
    print("Plaintext:", plaintext.decode())