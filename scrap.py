import os
import sys

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except Exception:
    print("Missing required packages: selenium, webdriver-manager, beautifulsoup4.")
    print("Install them with:")
    print("  python -m pip install --upgrade pip")
    print("  python -m pip install selenium webdriver-manager beautifulsoup4")
    print("Or install all at once with: python -m pip install -r requirements.txt")
    sys.exit(1)

from bs4 import BeautifulSoup
import time

def scrap(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Navigate to the url
        print(f"Opening {url}")
        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'article[data-testid="tweet"]')
            )
        )

        # get page source and parse the unorganize code into html format
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # find the mainc tweet using a specific selector
        main_tweet = soup.find("article", attrs={"data-testid": "tweet"})

        # get the tweet content
        if main_tweet:
            tweet_content = main_tweet.get_text(separator="\n", strip=True)

            lines = tweet_content.split("\n")
            display_name = lines[0] if len(lines) > 0 else "Unknown user"
            handle = lines[1] if len(lines) > 1 else ""
            username_line = f"{display_name} - {handle}"

            # exclude the first two lines(username) and the last 5 lines(time and date)
            content_lines = lines[2:-9] if len(lines) > 11 else lines[2:]
            content = "\n".join(content_lines).strip()

            formatted_content = f"{username_line}\n\n{content}"
            print("Content found successfully!")

            # defining the directory and file name
            dir_name = "Data"
            file_name = "Data.md"

            # create a full path to the file
            path = os.path.join(dir_name, file_name)

            # creating a directory
            os.makedirs(dir_name, exist_ok=True)

            with open(path, "w") as file:
                file.write(formatted_content)

            print(formatted_content)

            print(f"Content saved in {path}")
        else:
            print("Could not find the main tweet on the page")

    finally:
        driver.quit()
        print("Script end")


if len(sys.argv) > 1:
    url = sys.argv[1]
    scrap(url)
else:
    print("Please provide a Twitter URL as a command line argument")
    print('Example: python your_script_name.py "https://twitter.com/user/status/12345"')
