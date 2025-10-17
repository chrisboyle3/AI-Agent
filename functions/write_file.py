import os

def write_file(working_directory, file_path, content):
    try:
        # Combine working_directory with file_path
        target_path = os.path.join(working_directory, file_path)

        # Get absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(target_path)

        # Check if target_path is outside of working_directory
        if not abs_target_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure parent directories exist
        os.makedirs(os.path.dirname(abs_target_path), exist_ok=True)

        # Write (overwrite) content
        with open(abs_target_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
