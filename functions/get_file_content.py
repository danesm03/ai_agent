import os 
from google import genai
from google.genai import types


def get_file_content(working_directory, file_path):
        MAX_CHARS = 10000

        full_path  = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        if  not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isfile(full_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        try:
            with open(full_path) as f:
                file_content_string = f.read(MAX_CHARS + 1)
                if len(file_content_string) > MAX_CHARS: 
                    return file_content_string + f'...File "{file_path}" truncated at 10000 characters'
        except Exception as e:
             return f"Error:{e}"
        return file_content_string
                  
             
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="List content of specified files within your working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["directory"], 
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to the file you are pulling content from, relative to the working directory.",
        
            ),
        },
    ),
)