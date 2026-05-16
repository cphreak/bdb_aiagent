import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

import os
from google.genai import types
from config import MAX_CHARS


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of a file relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name of file to list the contents of, relative to the working directory.",
            ),
        },
    ),
)


def get_file_content(working_directory, file_path):

    try:
        absolute_dir = os.path.abspath(working_directory)
        # print(absolute_dir)
        target_file = os.path.normpath(os.path.join(absolute_dir, file_path))
        # Will be True or False
        if os.path.commonpath([absolute_dir, target_file]) != absolute_dir:
            raise RuntimeError(f'Cannot read "{file_path}" as it is outside the permitted working directory')
            
        if (os.path.isfile(target_file) == False):
            raise RuntimeError(f'File not found or is not a regular file: {file_path}')
            
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'
            else: 
                return(file_content_string)


        # for f in os.scandir(target_file):
        #     print(f'-{f.name}: file_size={f.stat().st_size} bytes, is_dir={f.is_dir()}')


    except Exception as e:
        return(f"Error: {e}")






def main():
    get_file_content("calculator", "lorem.txt")

if __name__ == "__main__":
    main()