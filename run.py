import init
import os
# checks if windows system and runs the program in a cmd instance
if os.name == 'nt':
    print("Program is running in another cmd window.")
    os.system('start cmd /K py initialize.py')
else:
    init.initialize()
# if its unix/unix-like system it runs it in the current shell session
