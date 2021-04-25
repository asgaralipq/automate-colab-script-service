import time
import os
import pyinotify,subprocess
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

# options = Options()
# options.headless = True
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results

# options.add_argument("--disable-extensions")
# # options.add_argument("user-data-dir=/home/asgaralipq/.config/chromium/Profile 1/")
# wd = webdriver.Chrome(options=options)
fp = webdriver.FirefoxProfile('/home/asgaralipq/.mozilla/firefox/0zhbal6h.default-release')
wd = webdriver.Firefox(fp)
# wd.get("https://colab.research.google.com/drive/1PIybc8oaszBcVeAPVQyAl-90jYDDMhWp")
wd.get("https://colab.research.google.com/drive/whatever")
print(wd.title)  
print("Page loaded")

wd.implicitly_wait(10)

wd.find_element_by_id('runtime-menu-button').click()
wd.find_element_by_id(':1v').click()
print("Running colab...")

wm = pyinotify.WatchManager()
wm.add_watch('/home/asgaralipq/Work/Colab-Script/Downloads/', pyinotify.ALL_EVENTS)
notifier = pyinotify.Notifier(wm)

time.sleep(3)

# if notifier.check_events():
#     time.sleep(3)
#     notifier.stop()
# else:
#     print("Waiting....")
#     time.sleep(3)
#     notifier.loop()

print("Waiting....")
notifier.loop()
os.kill(os.getpid(),signal.SIGINT)

print("Done")
notifier.stop()

time.sleep(5)

wd.quit()


# actions = ActionChains(wd).send_keys(Keys.CONTROL, Keys.ENTER).perform()
# divs = wd.find_elements_by_css_selector('div')