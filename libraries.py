import os
import sys


my_folder = os.getcwd()
print(my_folder)

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(entry.name)


arguments = sys.argv
print(arguments)

print(f"We're running on: {sys.platform}")
