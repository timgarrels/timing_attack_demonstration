import sys
import hashlib
import random


PASSWORD = "c567f5ce8bf72882743cf16bb78506fd6292561b11ff005765d9903b54fcd51f19b92d1c78b770c355792e2232dd05da66a4da122fe2b8cd76ee7ab0372716ad39d8728e7812875f3fe9562d3a2b806d17807f0960bc2c11c52cbecb9f5d0e1b8b56c6bff98282f1a6f1e3dcaf46b6d9f5ded95c36a47609b5f5a585b354e8c05f5072553487968d3df7b21449a37188ba61fcc5d7d6ba418b1999a212d976d0"

def create_password(length=5, ALPHABET=list("0123456789")):
    """Creates a pseudo-random password by appending random hashes"""

    password = ""
    for n in range(length):
        c = random.choice(ALPHABET)
        password += hash_character(c)

    print(password)
    

def hash_character(c):
    """This is hashing the character 100k times. It's super secure!"""

    h = c.encode()
    for n in range(100000):
        h = hashlib.sha256(h).digest()
    return h.hex()

def password_compare(password):
    """This compares each character hash of the given password with the stored one"""

    for idx, c in enumerate(password):
        current_hash_slice = PASSWORD[64*idx : 64*(idx+1)]
        if hash_character(c) != current_hash_slice:
            return False
    return True

def main():
    # Input Check
    if len(sys.argv) != 2:
        print("Usage: python3 timing_vuln.py login [password]")
        return -1

    # Sensitive Information
    if password_compare(sys.argv[1]):
        print("Access granted")
        print("This is just a demo")
    else:
        print("Access denied")

    
if __name__ == "__main__":
    main()