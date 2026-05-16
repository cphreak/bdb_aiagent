import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

from functions.get_file_content import get_file_content as get_file_content


get_file_content("calculator", "main.py")
get_file_content("calculator", "pkg/calculator.py")
get_file_content("calculator", "/bin/cat") 
get_file_content("calculator", "pkg/does_not_exist.py")