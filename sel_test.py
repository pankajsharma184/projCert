from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"

# go to PHP site and click the 'About Us' link
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

driver.get("http://172.27.86.151:32770/index.php")
driver.find_element_by_id("About Us").click()
driver.save_screenshot('test.png')
test = driver.page_source
if "Lorem Ipsum Dipsum" in test:
    print("Text is present on the page")
else:
    print("Text is NOT present on the page")
driver.quit()
