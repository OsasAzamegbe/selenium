from selenium import webdriver


# download chrome driver for you google chrome verion from: 
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# path to chrome driver executable on local system
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

# Instatiate web driver
driver = webdriver.Chrome(PATH)

url = "https://www.linkedin.com/"
driver.get(url)

email = driver.find_element_by_id("session_key")
password = driver.find_element_by_id("session_password")