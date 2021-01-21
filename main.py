from selenium import webdriver


# download chrome driver for you google chrome verion from: 
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# path to chrome driver executable on local system
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

# Instatiate web driver
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")