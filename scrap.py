import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# profile url we want to visit
URL = "https://x.com/yourclouddude/status/1973463347895861267"

# set up and launch the chrome browser
print("Launching browser....")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the url
print(f"Opening {URL}")
driver.get(URL)

# waiting for the page to load
time.sleep(5)

# get page source and parse the unorganize code into html format
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# find the mainc tweet using a specific selector
main_tweet = soup.find("article", attrs={"data-testid": "tweet"})

# get the tweet content
if main_tweet:
    tweet_text = main_tweet.get_text(strip=True)
    print(tweet_text)
else:
    print("Could not find the main tweet on the page")

driver.quit()
print("Script end")
