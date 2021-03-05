import os

dir = input("Enter the path: ")
filename = input("Enter filename: ")

for root, dirs, files in os.walk(dir):
    for file in files:
        if file == filename:
            print(os.path.join(root, file))