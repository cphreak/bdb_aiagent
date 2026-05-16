import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

from functions.get_files_info import get_files_info as get_files_info

get_files_info("calculator", ".")
get_files_info("calculator", "pkg")
get_files_info("calculator", "/bin")
get_files_info("calculator", "../")