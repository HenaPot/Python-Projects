from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = "G:/Arhiva/Chromedriver/chromedriver-win64/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("executable_path=" + chromedriver_path)

driver = webdriver.Chrome(options=options)
wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url="https://www.youtube.com/")

'''
articles_number = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(articles_number.text)
articles_number.click()
anyone_can_edit = driver.find_element(by=By.LINK_TEXT, value="anyone can edit")
anyone_can_edit.click()
'''

search = driver.find_element(by=By.ID, value="search")
print(search.is_displayed())
#search.send_keys("Python")

time.sleep(5)
driver.quit()