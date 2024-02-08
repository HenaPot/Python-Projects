from selenium import webdriver
from selenium.webdriver.common.by import By
#import time

chromedriver_path = "G:/Arhiva/Chromedriver/chromedriver-win64/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("executable_path=" + chromedriver_path)

driver = webdriver.Chrome(options=options)

headset_url = "https://www.amazon.com/BENGOO-G9000-Controller-Cancelling-Headphones/dp/B01H6GUCCQ/ref=sr_1_3?keywords=gaming+headsets&pd_rd_r=3a0a9488-ab53-48b2-89d0-82fe7518f05a&pd_rd_w=QNs3T&pd_rd_wg=1GYmP&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=TMCW8TSNANKYW1FMV7GM&qid=1690034417&sr=8-3"
pythonorg_url = "https://www.python.org/"
driver.get(url=pythonorg_url)

#used with headset_url
''' symbol = driver.find_element(by="class name", value="a-price-symbol")
whole_number = driver.find_element(by="class name", value="a-price-whole")
fraction_number = driver.find_element(by="class name", value="a-price-fraction")
price = symbol.text + whole_number.text + "." + fraction_number.text '''

#gets a link through css selecting an anchor tag inside a particular class, pythonorg_url
'''documentation_link = driver.find_element(by="css selector", value=".documentation-widget a")
print(documentation_link.get_attribute("href"))'''

#pythonorg_url
'''submit_bug = driver.find_element(by="xpath", value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_bug.get_attribute("href"))'''

#Challenge 1

my_dict = {}

for i in range(1, 6):
    xpath = f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a'
    time_xpath = f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time'
    name = driver.find_element(by=By.XPATH, value=xpath)
    time = driver.find_element(by=By.XPATH, value=time_xpath)
    #print(entry.text)
    my_dict[i-1] = {"time": time.get_attribute("datetime")[:10], "name": name.text}

print(my_dict)

#angela's way, doesn't work anymore due to changes on the website, these are just some snippets that work

#drills down from div that uniquely identifies event widget to time tag
'''elements = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
for element in elements:
    print(element.text)'''

driver.quit()

