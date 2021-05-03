import subprocess

file = input("choose file: ")
subprocess.call(f"{file}.py", shell=True)