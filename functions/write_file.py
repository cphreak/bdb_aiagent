import sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')

import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name of file to write the content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file, file_path"
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):

    try:
        absolute_dir = os.path.abspath(working_directory)
        # print(absolute_dir)
        target_file = os.path.normpath(os.path.join(absolute_dir, file_path))
        # Will be True or False
        if os.path.commonpath([absolute_dir, target_file]) != absolute_dir:
            raise RuntimeError(f'Cannot write to "{file_path}" as it is outside the permitted working directory')

        if os.path.isdir(target_file) == True:
            raise RuntimeError(f'Cannot write to "{file_path}" as it is a directory')

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f_write_len = f.write(content)
            if f_write_len == len(content):
                result = (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
            else:
                result = (f'Error: write failed')

        return result

    except Exception as e:
        return(f"Error: {e}")


def main():
    write_file("calculator", "crap.txt", "boo")

if __name__ == "__main__":
    main()