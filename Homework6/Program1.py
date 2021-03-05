import sys,os

filename = input("Enter file name: ")

while os.path.exists(filename) == True:
    print("True")
else:
    print("False")