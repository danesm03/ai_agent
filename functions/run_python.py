import os
import subprocess
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path  = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abs = os.path.abspath(working_directory)
    arglist_1 = ["python3",full_path]
    arglist_2 = arglist_1 + args

    #checks for file existence, proper directory placement and validates that it's a Python file
    try:
        if  not full_path.startswith(working_directory_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
    except Exception as e:
        return f'Error:{e}'
    

    try:
        result = subprocess.run(
            args=arglist_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30, cwd=working_directory_abs
            )
        
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        if len(result.stdout) == 0:
            return "No output produced"

        return f'STDOUT:{result.stdout} STDERR:{result.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs specified python script, constrained to working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["directory"], 
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory pointing to the python file you are trying to run. Relative to the working directory",
        
            ),
        },
    ),
)    