from selenium import webdriver

driver = webdriver.Chrome()
data = driver.get("https://x.com/yourclouddude/status/1973463347895861267")

print(data)
