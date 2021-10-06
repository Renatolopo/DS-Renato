# %%
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import re

links = {
    'tecnologia' : 'https://g1.globo.com/economia/tecnologia/',
    'politica' : 'https://g1.globo.com/politica/',
    'economia' : 'https://g1.globo.com/economia/',
    'mundo' : 'https://g1.globo.com/mundo/',
    'educacao' : 'https://g1.globo.com/educacao/',
}


# %%
option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'./geckodriver')

# %%
driver.get(links['economia'])
sleep(10)
driver.close()
# %%
