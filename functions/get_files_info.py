import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
        full_path  = os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs = os.path.abspath(working_directory)
        message = [] 
        if  not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if os.path.isdir(full_path) == False:
            return f'Error: "{directory}" is not a directory'
        
        for file in os.listdir(full_path):
            message.append(f"- {file}: file_size={os.path.getsize(os.path.join(full_path, file))} bytes, is_dir={os.path.isdir(os.path.join(full_path, file))}")
        
        return '\n'.join(message)



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["directory"], 
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
        
            ),
        },
    ),
)



