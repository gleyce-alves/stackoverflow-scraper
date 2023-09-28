import requests
from bs4 import BeautifulSoup
import re

def search_stack_overflow_error(api_key: str, search_query: str) -> list:
    """
    Search Stack Overflow for a specific error message.

    Args:
        api_key (str): Your Stack Overflow API key.
        search_query (str): The error message you want to search for.

    Returns:
        list: A list of dictionaries containing search results with titles and links.
    """

    # Split the search query into individual words and build a search string
    search_words = re.findall(r'\w+', search_query)
    search_string = ' '.join(search_words)

    params = {
        'site': 'stackoverflow',
        'key': api_key,
        'intitle': search_string,
    }

    api_url = 'https://api.stackexchange.com/2.3/search'

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])

        if not items:
            print("No results found for the search.")
        else:
            results = []
            for index, item in enumerate(items, start=1):
                title = item.get("title", "")
                link = item.get("link", "")
                results.append({"Title": title, "Link": link})
            return results
    else:
        print("Error in the request:", response.status_code)
        return []

def extract_answer_from_question_page(url: str) -> str:
    """
    Extract the answer from the first question page.

    Args:
        url (str): The URL of the question page.

    Returns:
        str: The answer text, or a message if no answer is found.
    """

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        answer_element = soup.find(class_="answer")

        if answer_element:
            answer_text = answer_element.find(class_="s-prose").get_text()
            return answer_text

        return "No answer found for the question."
    else:
        print("Error in the request:", response.status_code)
        return "Error in the request."
