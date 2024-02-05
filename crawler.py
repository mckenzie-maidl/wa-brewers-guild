from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\david.chen\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3
options.add_argument(r'--executable-path=C:\Users\david.chen\Downloads\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(options=options)
driver.get("https://untappd.com/192BrewingCo")
html_source = driver.page_source
with open("temp.html", 'w') as f:
    f.write(html_source)