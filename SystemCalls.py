
#!/usr/bin/python3

import os
from subprocess import call

# os is one of the coolest library available in Python
print("Current working directory:")
print(os.getcwd())

print("Current User:")
print(os.getuid())

print("PATH environment variable")
print(os.getenv("PATH"))

# Run raw os system command
os.system("ls -lah")

#  print directory using call
#inp = input("Hit Enter")


# call uses a tuple
call(["ls", "-lah"])