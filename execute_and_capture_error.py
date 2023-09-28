import subprocess
import re

def execute_script_and_capture_error(script_name):
    try:
        result = subprocess.run(["python3", script_name], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as error:
        captured_error = error.stderr
        print(f"The encountered error was:\n{captured_error}")
        return captured_error
    else:
        script_output = result.stdout
        print(f"Script output:\n{script_output}")
        return None

if __name__ == "__main__":
    script_name_to_execute = "error.py"
    captured_error = execute_script_and_capture_error(script_name_to_execute)

    if captured_error:
        # Use regular expression to extract the error message from the traceback
        error_match = re.search(r'(\w+Error: .+)', captured_error)
        if error_match:
            error_message = error_match.group(1)
            print(f"Captured error message:\n{error_message}")
        else:
            print("Error message not found in the traceback.")
