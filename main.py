from selenium import webdriver
from time import sleep

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69120074057586%2C%22north%22%3A37.85928662873102%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSegz4h_x8m_hCITroqb3SIk0A7yAp3oQmeeM5QEd24U3pduqA/viewform?usp=sf_link"
CHROMEDRIVER_PATH = "c:/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.get(URL)
sleep(2)

def get_prices():
    prices = []
    price = driver.find_elements_by_class_name("list-card-price")
    for i in price:
        n = i.text
        n = n.replace("$", "")
        n = n.replace(",", "")
        n = n.split('+')[0]
        n = n.split('/')[0]
        n = n.split(' ')[0]
        prices.append(int(n))
    return prices

def get_links():
    links = []
    link = driver.find_elements_by_class_name("list-card-link")
    for i in link:
        links.append(i.get_attribute('href'))
    links = links[::2]
    return links

def get_adrs():
    adrs = []
    adr = driver.find_elements_by_class_name("list-card-addr")
    for i in adr:
        adrs.append(i.text)
    return adrs

def send_form(n):
    driver.get(FORM)
    inputs = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    input_adr = inputs[0].send_keys(adrs[n])
    input_price = inputs[1].send_keys(prices[n])
    input_link = inputs[2].send_keys(links[n])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    submit.click()
    again = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    again.click()

adrs = get_adrs()
prices = get_prices()
links = get_links()

for i in range(len(adrs)):
    send_form(i)







# bs4 =====================

# import requests
# import lxml
# from bs4 import BeautifulSoup


# response = requests.get(URL)
# website_html = response.text
# soup = BeautifulSoup(website_html, "lxml")
#
# price = soup.find(class_="list-card-price")
# print(price) #왜 None만 나오는 거지? 아마존과 같은 현상이다. 이렇게 된거 selenium으로 간다.
