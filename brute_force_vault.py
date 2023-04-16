#!/usr/bin/env python3

import subprocess
import string

#function has 3 inputs: 'passwords' is a list which will have all passwords the function creates
def generate_passwords(length, current_password, passwords): 

    #test function to check length (there is no password at all)
    if length==0: 
        passwords.append(current_password) #adds the current password to list of passwords we're keeping track of
        return
    for char in string.ascii_lowercase: #loop to go through all lowercase letters in alphabet one at a time
        generate_passwords(length-1, current_password + char, passwords) #telling the function to keep making more passwords but they'll be one shorter and with a new letter at the end

def try_password(password): #takes password input and runs vault.o with the password as the argument
    result = subprocess.run(["./vault.o", password], capture_output=True)
    return result.stdout.strip()

def brute_force_vault(): #assumes the password is 1 character long
    password_length = 1
    success_msg = "Success"

    while True: #loop to keep trying lengths until it finds correct password
        print(f"Trying passwords of length {password_length}")
        passwords = []
        generate_passwords(password_length, "", passwords) #creates a list of all passwords with the current length

        for password in passwords:#loops over all passwords in the list and tries each one using 'try_passwords' function
            result = try_password(password)
            #print (f"trying: {password} -> {result}")

            if result == success_msg: #if output matches success_msg password is correct
                return password
                
        password_length +=1 #increments the length to try passwords of the next length

#block of code runs brute_force_vault() only if the script is being run as the main program, prints the correct password to console
correct_password = brute_force_vault()
print (f"Found correct password: {correct_password}")

