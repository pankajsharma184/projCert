from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options, service_args=['--verbose', '--log-path=/home/chromedriver.log'])

f = open("./ip.txt","r")
line = f.readline()
f.close()
port = line.split("/n")[0]

driver.get("http://172.27.86.151:"+port+"/index.php")
print(driver.title)
driver.find_element_by_id("About Us").click()
driver.save_screenshot('test.png')
test = driver.page_source
if "Lorem Ipsum Dipsum" in test:
    print("Text is present on the page")
else:
    print("Text is NOT present on the page")
driver.quit()
