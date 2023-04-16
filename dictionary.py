#!/usr/bin/env python3

#library which allows the script to run external programs and interact with them
import subprocess

#function takes a password as the input and runs the vault.o file with the password in it
def try_password(password):
    result = subprocess.run(["./vault.o", password], capture_output=True)
    return result.stdout.strip()
    
#function is responsible for finding the correct password, defines the success message as "Success"
def brute_force_vault(): 
    success_msg = "Success"
    
    # Read words from words_alpha.txt and stores them in a list called words
    with open('words_alpha.txt', 'r') as file:
        words = file.readlines()

    for word in words: 
        # Remove the newline character from the word
        word = word.strip()
        
        #for reach word call try_password function and prints the word and result output of vault.o program
        result = try_password(word) 
        print(f"Trying: {word} -> {result}")

#if result is equal to success message return the word
        if result == success_msg: 
            return word

    print("No password found in the dictionary") 

#script calls the brute_force_vault function and if the right password is found print the message below with the password
if __name__ == "__main__": 
    correct_password = brute_force_vault()
    if correct_password:
        print(f"Found correct password: {correct_password}") 
