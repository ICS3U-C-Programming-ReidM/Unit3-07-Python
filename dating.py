#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program checks if the user can date their grandchild
def dating_program():
    try:
        # Prompt the user to enter their age and convert it to an integer
        user_age = int(input("Enter your age: "))
        
        # Check if the age is between 25 and 40 (exclusive)
        if 25 < user_age < 40:
            print("You can date their grandchild!")
        else:
            print("Sorry, you cannot date their grandchild.")
    
    # Catch any ValueError that occurs if the input is not a valid integer
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")

# Call the function to run the program
dating_program()
