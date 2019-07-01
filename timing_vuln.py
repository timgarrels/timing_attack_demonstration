import sys

# Hardcoded Passphrase
PASSWORD = "12345678"


def insecure_string_compare(string1, string2):
    for idx, c in enumerate(string1):
        if string2[idx] != c:
            return False
    return True

def main():
    # Input Check
    if len(sys.argv) != 2:
        print("Usage: python3 timing_vuln.py [password]")

    # Sensitive Information
    if insecure_string_compare(SECRET, sys.argv[1]):
        print("Access granted")
        print("This is just a mock up")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()