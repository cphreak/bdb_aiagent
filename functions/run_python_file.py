import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a Python file located relative to the working directory. The python file can take multiple arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file to run, relative to the working directory.",
            ),
            # "args": types.Schema(
            #     type=types.Type.ARRAY,
            #     "items": types.Schema(
            #         "args":types.Type.STRING,
            #         description="Arguments to the run the Python file with."
                
            #     ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Arguments to run the Python file with.",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
    ),
)




def run_python_file(working_directory, file_path, args=None):

    result = ""
    try:
        absolute_dir = os.path.abspath(working_directory)
        # print(absolute_dir)
        target_file = os.path.normpath(os.path.join(absolute_dir, file_path))
        # Will be True or False
        if os.path.commonpath([absolute_dir, target_file]) != absolute_dir:
            raise RuntimeError(f'Cannot execute "{file_path}" as it is outside the permitted working directory')

        if os.path.isfile(target_file) == False:
            raise RuntimeError(f'"{file_path}" does not exist or is not a regular file')

        file_root, file_extension = os.path.splitext(file_path)
        if file_extension != ".py":
            raise RuntimeError(f'"{file_path}" is not a Python file')


        command = ["python", target_file]
        if args != None:
            command.extend(args)
        
        cp = subprocess.run(command, capture_output = True, cwd = absolute_dir, text = True, timeout = 30)
        if cp.returncode != 0:
            result += f"Process exited with code {cp.returncode}\n"
        if ( cp.stdout == "" ) and ( cp.stderr == "" ):
            result += f"No output produced\n"
        else: 
            result += f"STDOUT:{cp.stdout}\n"
            result += f"STDERR:{cp.stderr}\n"

        # print(result)
        return result

    except Exception as e:
        return (f"executing Python file: {e}")


def main():
    run_python_file("calculator", "main.py")

if __name__ == "__main__":
    main()
