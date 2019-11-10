import time
from selenium import webdriver
'''
//*[@id="search"]
//*[@id="container"]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[1]/input
//*[@id="container"]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[1]/input
'''

def getPrice(address):
    driver = webdriver.Chrome('D:\ChromeDriverIsolate\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get('http://www.gasbuddy.com/');
    search_box = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[1]/input')
    search_box.send_keys(address)
    search_box.submit()
    time.sleep(2) #ensure page is loaded
    price_container = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[4]/div/span')
    price = price_container.text
    driver.quit()
    return price
print(getPrice('6 River Rd, Summit, NJ 07901, United States'))
