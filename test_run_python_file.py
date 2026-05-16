import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

from functions.run_python_file import run_python_file as run_python_file


run_python_file("calculator", "main.py")
run_python_file("calculator", "main.py", ["3 + 5"]) 
run_python_file("calculator", "tests.py") 
run_python_file("calculator", "../main.py") 
run_python_file("calculator", "nonexistent.py") 
run_python_file("calculator", "lorem.txt") 