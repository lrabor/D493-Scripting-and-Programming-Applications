import requests
import xml.etree.ElementTree as ET

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

def get_xml_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        print("\nXML Data Fetched Successfully")
        return root
    elif response.status_code == 404:
        print(f"Resource not found")
    elif response.status_code == 500:
        print(f"Server error, try again later.")
    else:
        print(f"Error fetching XML data: {response.status_code}")

    return None

def parse_xml_data(root):
    xml_info = {}
    if root is not None:
        to = root.find('to').text if root.find('to') is not None else "N/A"
        from_ = root.find('from').text if root.find('from') is not None else "N/A"
        heading = root.find('heading').text if root.find('heading') is not None else "N/A"
        body = root.find('body').text if root.find('body') is not None else "N/A"

        xml_info = {
            "To": to,
            "From": from_,
            "Heading": heading,
            "Body": body

        }
    return xml_info

def parse_json_data(data):
    users_info = []
    for user in data[:3]:
        user_data = {
            "ID": user.get('id'),
            "Name": user.get('name'),
            "Email": user.get('email')
        }
        users_info.append(user_data)

    return users_info


def display_json_data(users_info):
    """Displays key information from parsed JSON data."""
    if users_info:
        print("🔹 Extracting JSON Data:\n")
        for user in users_info:  # Display each user's info from the list
            print(f"👤 ID: {user['ID']}, Name: {user['Name']}, Email: {user['Email']}")


def display_xml_data(xml_info):
    if xml_info:
        print("\nExtracting XML Data:\n")
        for key, value in xml_info.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    JSON_API_URL = "https://jsonplaceholder.typicode.com/users"
    XML_API_URL = "https://raw.githubusercontent.com/lrabor/webinar-files/main/note.xml"

    json_data = get_json_data(JSON_API_URL)
    users_info = parse_json_data(json_data)
    display_json_data(users_info)

    xml_root = get_xml_data(XML_API_URL)
    xml_info = parse_xml_data(xml_root)
    display_xml_data(xml_info)