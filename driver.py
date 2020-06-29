from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': os.getcwd() + '/' + 'renders'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

URL = 'https://app.viddyoze.com/templates'

driver.get(URL)
