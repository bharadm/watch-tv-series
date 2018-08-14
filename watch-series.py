import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen
import csv
import watchseriesinsert as ws
driver = webdriver.Chrome("C:/Users/Bharadwaj/Downloads/chromedriver.exe")
url_website = str(input("Give url link: "))
driver.get(url_website)
i = -1
list = []
while i != 0:
    print("Give search command ")
    elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/input")
    elem.clear()
    elem.send_keys(str(input()))
    elem.send_keys(Keys.RETURN)
    count = 0
    sauce = Request(str(driver.current_url), None,{'User-Agent': 'Mozilla/5.0'})
    website = urlopen(sauce)
    soup = bs.BeautifulSoup(website, 'lxml')
    print("Select \n")
    for link in soup.find_all('div', {'class':'wrap'}):
        #print(link.find('a')['href'])
        list.insert(count,link.find('a')['href'])
        print(str(count)+". "+(link.find('h5')['title']))
        count = count+1
    print("-1. Search again")
    print("-2. Exit")
    value = int(input(""))
    if value>=0:
        ws.insert_method(list[value])
        break
    elif value==-2:
        exit(0)
