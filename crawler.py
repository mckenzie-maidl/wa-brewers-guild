from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

data = pd.read_excel('WA Breweries.xlsx')
links = data['Untappd Profile Link'].values
breweries = data['Brewery'].values

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\david.chen\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3
options.add_argument(r'--executable-path=C:\Users\david.chen\Downloads\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(options=options)

ratings = {}
for br, link in zip(breweries, links):
    try:
        driver.get(link)

        from selenium.webdriver.common.by import By
        elem = driver.find_element(By.XPATH, '//span[@class = "num"]')
        rating = float(elem.text[1:-1])
        ratings[br] = rating
    except:
        pass

data['rating'] = data['Brewery'].map(ratings)
data.to_excel('WA Breweries.xlsx', index = False)