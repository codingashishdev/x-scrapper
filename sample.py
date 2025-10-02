import requests
from bs4 import BeautifulSoup

url = "https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"
response = requests.get(url)

# check id the request was successfull (200 denotes ok)
if response.status_code == 200:
    # parse the html to make it look Beautiful
    soup = BeautifulSoup(response.text, "html.parser")

    # find the <title> tag and get the text
    page_title = soup.find("title").text
    print(f"The page title is: {page_title}")

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
