import subprocess

def execute_script_and_capture_error(script_name):
    try:
        result = subprocess.run(["python3", script_name], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as error:

        captured_error = error.stderr
        
        print(f"The encountered error was:\n{captured_error}")
    else:
        
        script_output = result.stdout
        print(f"Script output:\n{script_output}")

if __name__ == "__main__":
    script_name_to_execute = "error.py"
    execute_script_and_capture_error(script_name_to_execute)