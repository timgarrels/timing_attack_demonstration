import sys
import time

SECRET = "12345678"


def insecure_string_compare(string1, string2):
    for idx, c in enumerate(string1):
        if string2[idx] != c:
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 timing_vuln.py [password]")

    password = sys.argv[1]

    if insecure_string_compare(SECRET, password):
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()