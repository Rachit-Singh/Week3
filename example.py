#! /usr/bin/python3

def git_opeation():
    print("I am adding example.py file to the remote repository.")
    name = input("Enter a name: ")
    age = int(input())

    print("Your name is ", name)

    if age < 18 :
        print("You are not young")
    else :
        print("You are young")
    
git_opeation()

