import os

def get_files_info(working_directory, directory="."):
    try:
        # Build full path safely
        full_path = os.path.join(working_directory, directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(full_path)

        # Check if target directory is within working directory
        if not abs_target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if path is actually a directory
        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'

        # Build list of files with size and directory status
        entries = []
        for entry in os.listdir(abs_target_dir):
            entry_path = os.path.join(abs_target_dir, entry)
            try:
                file_size = os.path.getsize(entry_path)
                is_dir = os.path.isdir(entry_path)
                entries.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                entries.append(f"- {entry}: Error retrieving info ({e})")

        # Return all entries as one formatted string
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {e}"