import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        # Combine paths safely
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Security check: ensure file is inside the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # File existence check
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        # Must be a .py file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Run the Python file in a subprocess
        completed_process = subprocess.run(
            ["python", abs_file_path] + args,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )

        # Collect stdout and stderr
        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()

        # If no output at all
        if not stdout and not stderr:
            return "No output produced."

        # Build output string
        output = []
        if stdout:
            output.append(f"STDOUT:\n{stdout}")
        if stderr:
            output.append(f"STDERR:\n{stderr}")

        # Non-zero exit code
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
