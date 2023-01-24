from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate a new RSA key
# The script generates strong keys, as it uses
# the RSA.generate() method with a key length of 2048 bits,
# which is considered a secure key length for RSA encryption.
private_key = RSA.generate(2048)
public_key = private_key.publickey()

# Save the private key to a file
with open("private.pem", "wb") as f:
    f.write(private_key.export_key())

# Save the public key to a file
with open("public.pem", "wb") as f:
    f.write(public_key.export_key())

# Define the message to be encrypted
message = b'flag{Hi, this is an example for ISEP 2023 Project 2 CTF}'

# Create the cipher object and encrypt the message
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)

# Write the ciphertext to a file
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)

# Read the private key from the file
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Read the ciphertext from the file
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()

# Create the cipher object and decrypt the ciphertext
cipher = PKCS1_OAEP.new(private_key)
plaintext = cipher.decrypt(ciphertext)

# Check if the plaintext starts with "flag"
if plaintext.startswith(b"flag"):
    print("Flag:", plaintext.decode())
else:
    print("Plaintext:", plaintext.decode())