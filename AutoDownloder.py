# Created By Tejass3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe" # here Add the YOur path of the computer
driver = webdriver.Chrome(PATH) # this is path of the Chrome Driver
driver.get("https://gogoanime.ai/")
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, 1000);") # for scrolling down the page
link = driver.find_element_by_link_text("Shingeki no Kyojin: The Final Season") # In this bracket Anime Name
link.click()
link2 = driver.find_element_by_link_text("Download").click()
p = driver.current_window_handle

#get first child window
chwd = driver.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
        driver.switch_to.window(w)
        DOW = driver.find_element_by_class_name("dowload").click()
        
time.sleep(5)
