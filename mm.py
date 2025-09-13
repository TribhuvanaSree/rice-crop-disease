import subprocess
import sys


output = subprocess.check_output('python p1.py', shell=True)

print(output)