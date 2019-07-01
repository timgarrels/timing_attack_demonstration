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



def timing_attack(command, tries=1000):
    durations = []

    for n in range(tries):
        print("Executing", command, "for the", n, "-th time")

        start = time.time()

        p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        duration = time.time() - start
        durations.append(duration)
        
    return durations

def avg(l):
    return sum(l)/len(l)

def main():

    tries = 200

    correct_password = "12345678"
    wrong_password = "12045678"

    correct_cmd = " ".join(["python3", "timing_vuln.py", correct_password])
    wrong_cmd = " ".join(["python3", "timing_vuln.py", wrong_password])

    correct_duration_avg = avg(timing_attack(correct_cmd, tries))
    wrong_duration_avg = avg(timing_attack(wrong_cmd, tries))

    print(correct_duration_avg)
    print(wrong_duration_avg)


if __name__ == "__main__":
    main()
