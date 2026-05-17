import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

from functions.get_files_info import get_files_info as get_files_info

print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "/bin"))
print(get_files_info("calculator", "../"))