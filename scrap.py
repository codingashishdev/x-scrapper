import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# profile url we want to visit
URL = "https://x.com/nasa"

# set up and launch the chrome browser
print("Launching browser....")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the url
print(f"Opening {URL}")
driver.get(URL)

# keep the script running so that the browserr doesn't shutdown
print("Browser is open. Press enter in this terminal to close it")
input()

# close the browser
driver.quit()
print("Browser closed")
