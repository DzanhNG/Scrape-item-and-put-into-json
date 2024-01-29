from tabnanny import check
import requests
from bs4 import BeautifulSoup

url = "https://palworld.gg/pals"
response = requests.get(url)

list_linkto_pal = []
if response.status_code == 200:
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags
    links = soup.find_all('a')
    
    # Print the text content of each <a> tag
    for atag in links:
        href =  atag.get('href')
        if href[:5] == "/pal/":
            list_linkto_pal.append('https://palworld.gg' + href)
    print("list_linkto_pal: ", list_linkto_pal)
else:
    print(f"Failed to retrieve HTML. Status code: {response.status_code}")

