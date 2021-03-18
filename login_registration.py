import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()



#Registration_login регистрация аккаунта

# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id("menu-item-50").click()
# mail = driver.find_element_by_id("reg_email")
# mail_txt = str("qqqq@mail.ro")
# mail.send_keys(mail_txt)
# time.sleep(1)
# passw = driver.find_element_by_id("reg_password")
# passw_txt = "enrfgksdtn2"
# passw.send_keys(passw_txt)
# driver.find_element_by_css_selector("#customer_login>div:nth-child(2)>form>:nth-child(4)>input:nth-child(3)").click()
# driver.quit()

#Registration_login логин в систему

# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id("menu-item-50").click()
# mail = driver.find_element_by_id("username")
# mail_txt = str("qqqq@mail.ro")
# mail.send_keys(mail_txt)
# passw = driver.find_element_by_id("password")
# passw_txt = "enrfgksdtn2"
# passw.send_keys(passw_txt)
# driver.find_element_by_css_selector("div>div>div>form>p:nth-child(3)>input:nth-child(3)").click()
# logout_chk = WebDriverWait(driver, 1).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR,("#page-36>div>div>nav>ul>li:nth-child(6)>a")))
# )
# driver.quit()
