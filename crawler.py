from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

data = pd.read_csv('data/wa_breweries.csv')
links = data['untappd_profile_link'].values
breweries = data['brewery'].values

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\david.chen\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3
options.add_argument(r'--executable-path=C:\Users\david.chen\Downloads\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(options=options)

def num_handler(s):
    if type(s) == str:
        s =s.replace(',', '')
        if "M+" in s:
            s = s.replace('M+', "000000")
    return float(s)

ratings = {}; totalVisits = {}; uniqueVisits = {}; monthlyVisits = {}
for br, link in zip(breweries, links):
    try:
        driver.get(link)

        from selenium.webdriver.common.by import By
        elem = driver.find_element(By.XPATH, '//span[@class = "num"]')
        statsElem = driver.find_element(By.XPATH, '//div[@class = "stats"]')
        statsText = statsElem.text.split('\n')
        totalVisit = num_handler(statsText[1])
        uniqueVisit = num_handler(statsText[3])
        monthlyVisit = num_handler(statsText[5])
        stats = {'total': totalVisit, 'unique': uniqueVisit, 'monthly': monthlyVisit}
        rating = float(elem.text[1:-1])
        ratings[br] = rating
        totalVisits[br] = totalVisit
        uniqueVisits[br] = uniqueVisit
        monthlyVisits[br] = monthlyVisit
        stats['rating'] = rating
        print(stats)
    except:
        pass

data['rating'] = data['brewery'].map(ratings)
data['total_visits'] = data['brewery'].map(totalVisits)
data['unique_visits'] = data['brewery'].map(uniqueVisits)
data['monthly_visits'] = data['brewery'].map(monthlyVisits)
data.to_csv('data/wa_breweries_with_ratings.csv', index = False)
driver.quit()