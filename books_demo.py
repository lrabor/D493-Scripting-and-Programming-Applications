import requests

def get_json_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        print(f"Resource not found")
    elif response.status_code == 500:
        print(f"Server error, try again later.")
    else:
        print(f"Error: {response.status_code}")

    return None

def parse_json_data(data):
    """Parses the JSON data to extract relevant book info."""
    book_info = []
    if data:
        for book in data.get("docs", [])[:3]:  # 'docs' contains the list of books
            book_data = {
                "title": book.get("title"),
                "author": ", ".join(book.get("author_name", [])),  # Get authors from 'author_name'
                "published_date": book.get("first_publish_year"),
            }
            book_info.append(book_data)
    return book_info


def display_json_data(books_info):
    """Displays key information from parsed JSON book data in a structured format."""
    if books_info:
        print("Extracted Book Data:\n")
        for index, book in enumerate(books_info, start=1):
            print(f"Book {index}:")
            for key, value in book.items():
                print(f"\t{key.replace('_', ' ').title()}: {value}") #Published Date
            print("\n" + "-" * 40 + "\n")  # Separator for readability
    else:
        print("No book data available.")


if __name__ == '__main__':
    JSON_API_URL = "https://openlibrary.org/search.json?q=python"

    json_data = get_json_data(JSON_API_URL)
    users_info = parse_json_data(json_data)
    display_json_data(users_info)
