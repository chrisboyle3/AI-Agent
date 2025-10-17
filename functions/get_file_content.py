import os
from functions.config import MAX_FILE_CHARACTERS

def get_file_content(working_directory, file_path):
    try:
        # Resolve absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if file is outside working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if file exists and is a regular file
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Try to read file content
        with open(abs_file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Truncate if too long
        if len(content) > MAX_FILE_CHARACTERS:
            content = (
                content[:MAX_FILE_CHARACTERS]
                + f'\n[...File "{file_path}" truncated at {MAX_FILE_CHARACTERS} characters]'
            )

        return content

    except Exception as e:
        return f"Error: {e}"