import init
import os
if os.name == 'nt':
    print("Program is running in another cmd window.")
    os.system('start cmd /K py initialize.py')
else:
    init.initialize()
