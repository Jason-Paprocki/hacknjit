import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
from GasStation import GasStation
from lxml import etree

'''
//*[@id="search"]
//*[@id="container"]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[1]/input
//*[@id="container"]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[1]/input
Address = /html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[2]/div[2]
Price = /html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[4]/div/span

'''
'''
def get_price_at_address(address):
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('http://www.gasbuddy.com/')
    search_box = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[1]/input')
    search_box.send_keys(address)
    search_box.submit()
    time.sleep(2) #ensure page is loaded
    address_container = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[4]')
    print(address_container.text)
    price_container = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[4]/div/span')
    price = price_container.text

    driver.quit()
    return price
print(get_price_at_address('6 River Rd, Summit, NJ 07901, United States'))
'''

def format_address(address):
    fmt = ""
    for c in address:
        if c == ' ':
            fmt += '%20'
        elif c == ',':
            fmt += '%2C'
        else:
            fmt += c

    return fmt

def get_station_at_address(address):
    #send request to gasbuddy.com for best prices nearby
    url = 'http://www.gasbuddy.com/home'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    payload = {'search' : format_address(address),
               'fuel' : '1'}


    response = requests.get(url, params=payload, headers=headers, data="ON")

    #parse and prepare data
    html = response.text
    soup = BeautifulSoup(html, features='lxml')

    #build GasStation object to hold address and price

    dom = etree.HTML(html)
    price_text = dom.xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[4]/div/span/text()")
    address_text = dom.xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div[2]/div[2]/text()")
    print(price_text)
    print(address_text)


    '''
    gs_addr_cont_regex = re.compile("^(GenericStationListItem__address)")
    gs_address = soup.find_all('div')
    print("Station Address:", gs_address)
    gs_price_cont_regex = re.compile("^(GenericStationListItem__priceContainer)")
    gs_price = soup.find(gs_price_cont_regex).span
    print("Station Price:", gs_price)
    '''
    return GasStation(address_text, price_text)
