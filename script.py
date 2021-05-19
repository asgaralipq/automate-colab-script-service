import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

fp = webdriver.FirefoxProfile('/home/asgaralipq/.mozilla/firefox/0zhbal6h.default-release')
wd = webdriver.Firefox(fp)
wd.get("https://colab.research.google.com/drive/1PIybc8oaszBcVeAPVQyAl-90jYDDMhWp")
print(wd.title)  
print("Page loaded")

wd.implicitly_wait(10)
wd.find_element_by_id('runtime-menu-button').click()
wd.find_element_by_id(':1v').click()

print("Running colab...")
print("Waiting for task to complete...")

while not os.path.isfile('/home/asgaralipq/Work/Colab-Script/Downloads/copy.txt'):
    time.sleep(1)

print("Task completed")

time.sleep(5)

print("Closing Driver...")

wd.quit()