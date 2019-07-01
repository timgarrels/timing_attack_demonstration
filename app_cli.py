import sys

import app_security


PASSWORD_ALPHABET = list("0123456789")
PASSWORD_LENGTH = 3


def reset_password():
    print("Resetting password...")
    c_password, h_password = app_security.create_password(PASSWORD_LENGTH, PASSWORD_ALPHABET)
    with open("pwd", "w") as f:
        f.write(h_password)
    print("Reset done! Last digit: {last_digit}".format(last_digit=c_password[-1:]))
    print("TODO:", c_password)

def login():
    print("Trying to login...")
    # Sensitive Information

    with open("pwd", "r") as f:
        password = f.read()

    if app_security.password_compare(password, sys.argv[2]):
        print("Access granted")
        print("This is just a demo")
    else:
        print("Access denied")

def print_usage():
        print("Usage: python3 timing_vuln.py reset")
        print("Usage: python3 timing_vuln.py login [password]")

def invalid_option():
    print("Option not found!")
    print_usage()

def main():
    options = {"reset":(reset_password, 0), "login":(login, 1)}
    if len(sys.argv) < 2:
        print_usage()
    else:
        option, req_argn = options.get(sys.argv[1], (invalid_option, 0))
        if req_argn <= len(sys.argv) - 2:
            option()
        else:
            print_usage()
    
if __name__ == "__main__":
    main()
