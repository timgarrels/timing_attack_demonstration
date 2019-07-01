# Timing Attack Demonstration

A mock-up timing attack against character wise password comparison in Python.

Made for a presentation for a ISec-Seminar.

`timing_vuln.py` does a character wise string comparision. Upon reading a wrong character it will stop the comparison which leaks the information which character was wrong.

`timing_attack.py` exploits this leaked information to constuct a valid password.
