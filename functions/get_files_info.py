import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        absolute_dir = os.path.abspath(working_directory)
        # print(absolute_dir)
        target_dir = os.path.normpath(os.path.join(absolute_dir, directory))
        # Will be True or False
        if os.path.commonpath([absolute_dir, target_dir]) != absolute_dir:
            raise RuntimeError(f'Cannot list "{target_dir}" as it is outside the permitted working directory')
            
        if (os.path.isdir(target_dir) == False):
            raise RuntimeError(f'"{directory}" is not a directory')
            
        results = ""
        for f in os.scandir(target_dir):
            results += (f'-{f.name}: file_size={f.stat().st_size} bytes, is_dir={f.is_dir()}  ')
        return results

    except Exception as e:
        return(f"Error: {e}")

def main():
    get_files_info("calculator", ".")


if __name__ == "__main__":
    main()