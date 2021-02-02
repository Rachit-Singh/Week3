#! /usr/bin/python3

def git_opeation():
    print("I am adding example.py file to the remote repository.")
    yourName = input("Enter a name: ")
    age = int(input("Enter age: "))

    print("Your name is ", yourName)

    if age < 15 :
        print("You are a kid")
    elif age < 18 :
        print("You are young")
    else :
        print("You are adult")
    
git_opeation()

