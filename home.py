import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()



#Home: добавление комментария

driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0>div>ul>li>a>h3").click()
driver.find_element_by_css_selector("#content>div>div:nth-child(3)>ul>li:nth-child(2)").click()
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector("#respond>form>p:nth-child(2)>p>span>a:nth-child(5)").click()
comm = driver.find_element_by_id("comment")
rew_txt = str("Nice book!")
comm.send_keys(rew_txt)
name = driver.find_element_by_id("author")
name_txt = str("Buddy")
name.send_keys(name_txt)
mail = driver.find_element_by_id("email")
mail_txt = str("qqq@mail.ro")
mail.send_keys(mail_txt)
driver.find_element_by_id("submit").click()
driver.quit()

