"""
2.   https://demoqa.com/
2.1. https://www.awesomescreenshot.com/video/9449793?key=b6fade3e318c5369a2b4771f363433e7  воспроизвести действия
     с помощью Selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import TARGET_URL
import time

browser = webdriver.Chrome()
browser.get(TARGET_URL)
browser.maximize_window()
browser.implicitly_wait(5)

# Scrolling down but not to the very bottom
js = "var q=document.documentElement.scrollTop=200"
browser.execute_script(js)

# Click-on the Elements
element = browser.find_element(By.CSS_SELECTOR, '[stroke = "currentColor"]')
element.click()

# Click-on the Check Box
check_box = browser.find_element(By.ID, 'item-1')
check_box.click()
chb_home = browser.find_element(By.CLASS_NAME, 'rct-checkbox')
chb_home.click()

# Click-on the Radio Button
radio_button = browser.find_element(By.ID, 'item-2')
radio_button.click()
rb_impressive = browser.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]')
rb_impressive.click()
rb_yes = browser.find_element(By.CSS_SELECTOR, '[for="yesRadio"]')
rb_yes.click()

browser.quit()

# Run the code below if you want to see the result in real time (but comment out lines till 16 to 38 before this):

# js = "var q=document.documentElement.scrollTop=200"
# browser.execute_script(js)
# time.sleep(2)
#
# element = browser.find_element(By.CSS_SELECTOR, '[stroke = "currentColor"]')
# element.click()
# time.sleep(2)
#
# check_box = browser.find_element(By.ID, 'item-1')
# check_box.click()
# time.sleep(2)
# chb_home = browser.find_element(By.CLASS_NAME, 'rct-checkbox')
# chb_home.click()
# time.sleep(2)
#
# radio_button = browser.find_element(By.ID, 'item-2')
# radio_button.click()
# time.sleep(2)
# rb_impressive = browser.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]')
# rb_impressive.click()
# time.sleep(2)
# rb_yes = browser.find_element(By.CSS_SELECTOR, '[for="yesRadio"]')
# rb_yes.click()
# time.sleep(2)
#
# browser.quit()
