#!/usr/bin/python3
import itertools
import string
import subprocess
import time



 
def test_password(password):#takes a password as an input parameter and runs the ./vault.o program with the given password argument. It captures the output of the program using subprocess.run() and measures the response time of the program using time.perf_counter()
    start_time = time.perf_counter()
    result = subprocess.run(["./vault.o", password], capture_output=True)
    end_time = time.perf_counter()
    response_time = end_time - start_time
    return response_time, result.stdout.decode("utf-8") #returns response time and the output of the program in UTF-8 encoded string format

characters = string.ascii_lowercase

min_individual_threshold = .005  # Adjust this value to only process thresholds slower than a certain amount



def generate_password(): #function starts with an empty password and loops through all possible combinations of characters from a to z. It measures the response time of each combination using the test_password() function and selects the slowest character that exceeds the min_individual_threshold response time
    password = ""
    for length in range(1, 12):
        max_response_time = 0
        slowest_char = None
        for char in characters:
            test_pass = password + char
            response_time, output = test_password(test_pass)

            if response_time > max_response_time and response_time > min_individual_threshold:
                max_response_time = response_time
                slowest_char = char

        if slowest_char is not None:#It continues to add the slowest character to the password until the length of the password is 11 or the slowest character cannot be found.
            password += slowest_char
        else:
            break

    return password



while True: #infinite loop to generate passwords using the generate_password() function until a password of length 11 is found
    generated_password = generate_password()
    if len(generated_password) == 11: 
        response_time, output = test_password(generated_password) #measures the response time and output of the ./vault.o program using the test_password() function for the generated password
        print(f"Trying password: {generated_password} with delay: {response_time}")
        print(f"Output of vault.o: {output}")

        if "Wrong password" not in output: #password's output does not contain the string "Wrong password" If the condition is true, it means that the correct password has been found, and the program exits with a success code 0. If the condition is false, the program continues to generate passwords until the correct password is found.
            print(f"Password found: {generated_password}")
            exit(0)