import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'http://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract specific data from the HTML
    # For example, let's extract all the headings (h1 tags)
    headings = soup.find_all('h1')
    
    # Open a file to save the extracted data
    with open('headings.txt', 'w') as file:
        # Iterate over the extracted headings and write each one to the file
        for heading in headings:
            file.write(heading.get_text() + '\n')
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

