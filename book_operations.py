import requests

class BookData:
    def __init__(self, api_url):
        self.api_url = api_url
        #print(f"API URL set to: {self.api_url}")  # Print the API URL

    def get_json_data(self):
        """Fetches JSON data from the API."""
        response = requests.get(self.api_url)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Resource not found")
        elif response.status_code == 500:
            print("Server error, try again later.")
        else:
            print(f"Error: {response.status_code}")
        return None

    def parse_json_data(self, data):
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
