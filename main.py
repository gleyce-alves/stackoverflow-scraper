import re
import subprocess
from search_stackoverflow import search_stack_overflow_error, extract_answer_from_question_page

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

def search_solution_for_error(error_message):
    search_results = search_stack_overflow_error(api_key, error_message)

    if search_results:
        print("Search results:")
        for index, result in enumerate(search_results, start=1):
            print(f"{index}. Title: {result['Title']}")
            print(f"   Link: {result['Link']}")

        first_result = search_results[0]
        first_result_title = first_result['Title']
        first_result_link = first_result['Link']

        print(f"\nTitle of the first result: {first_result_title}")
        print(f"Link of the first result: {first_result_link}")

        answer = extract_answer_from_question_page(first_result_link)
        print(f"Answer from the first result: {answer}")
    else:
        print("No results found for the search.")

if __name__ == "__main__":
    api_key = 'X7)HB7SzXcSiziIw1QuOuA(('

    script_name_to_execute = "error.py"
    captured_error = execute_script_and_capture_error(script_name_to_execute)

    if captured_error:
        # Use regular expression to extract the error message from the traceback
        error_match = re.search(r'(\w+Error: .+)', captured_error)
        if error_match:
            error_message = error_match.group(1)
            print(f"Captured error message:\n{error_message}")
            
            search_solution_for_error(error_message)
        else:
            print("Error message not found in the traceback.")
