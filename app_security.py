import hashlib
import random
import time


def password_compare(password, login_try):
    """ This compares each character hash of the given password with the stored one """

    for idx, c in enumerate(login_try):
        current_hash_slice = password[64*idx : 64*(idx+1)]
        if hash_character(c) != current_hash_slice:
            return False
    return True

    
def hash_character(c):
    """ This is hashing the character 10k times. It's super secure! """
    h = c.encode()
    for n in range(10000):
        h = hashlib.sha256(h).digest()
    return h.hex()


def create_password(length, alphabet):
    """ Creates a pseudo-random password by appending random hashes """

    c_password = ""
    h_password = ""
    for n in range(length):
        c = random.choice(alphabet)
        c_password += c
        h_password += hash_character(c)

    return c_password, h_password