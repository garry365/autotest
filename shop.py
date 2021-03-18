import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

# Shop отображение страницы товара
# driver.find_element_by_id("menu-item-50").click()
# mail = driver.find_element_by_id("username")
# mail_txt = str("qqqq@mail.ro")
# mail.send_keys(mail_txt)
# passw = driver.find_element_by_id("password")
# passw_txt = "enrfgksdtn2"
# passw.send_keys(passw_txt)
# driver.find_element_by_css_selector("div>div>div>form>p:nth-child(3)>input:nth-child(3)").click()
# driver.find_element_by_css_selector("#menu-item-40>a").click()
# driver.find_element_by_css_selector("#content>ul>li:nth-child(3)>a>h3").click()
# book_name = "HTML5 Forms"
# book_name_chk = WebDriverWait(driver, 2).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR,("#product-181>div:nth-child(2)>h1")), book_name)
# )
# driver.quit()

# Shop количество товаров в категории

# driver.find_element_by_id("menu-item-50").click()
# mail = driver.find_element_by_id("username")
# mail_txt = str("qqqq@mail.ro")
# mail.send_keys(mail_txt)
# passw = driver.find_element_by_id("password")
# passw_txt = "enrfgksdtn2"
# passw.send_keys(passw_txt)
# driver.find_element_by_css_selector("div>div>div>form>p:nth-child(3)>input:nth-child(3)").click()
# driver.find_element_by_css_selector("#menu-item-40>a").click()
# driver.find_element_by_css_selector("#woocommerce_product_categories-2>ul>li:nth-child(2)>a").click()
# count = driver.execute_script("return document.getElementsByClassName('product').length")
# assert count == 3
# driver.quit()

# Shop сортировка товаров

# driver.find_element_by_id("menu-item-50").click()
# mail = driver.find_element_by_id("username")
# mail_txt = str("qqqq@mail.ro")
# mail.send_keys(mail_txt)
# passw = driver.find_element_by_id("password")
# passw_txt = "enrfgksdtn2"
# passw.send_keys(passw_txt)
# driver.find_element_by_css_selector("div>div>div>form>p:nth-child(3)>input:nth-child(3)").click()
# driver.find_element_by_css_selector("#menu-item-40>a").click()
# sel = driver.find_element_by_class_name("orderby")
# sel_chk = sel.get_attribute("value")
# assert sel_chk == "menu_order"
# sel_sort = Select(sel)
# sel_sort.select_by_value("price-desc")
# sel = driver.find_element_by_class_name("orderby")
# sel_chk = str(sel.get_attribute("value"))
# assert sel_chk == "price-desc"
# driver.quit()

# Shop отображение, скидка товара

# driver.find_element_by_id("menu-item-50").click()
# mail = driver.find_element_by_id("username")
# mail_txt = str("qqqq@mail.ro")
# mail.send_keys(mail_txt)
# passw = driver.find_element_by_id("password")
# passw_txt = "enrfgksdtn2"
# passw.send_keys(passw_txt)
# driver.find_element_by_css_selector("div>div>div>form>p:nth-child(3)>input:nth-child(3)").click()
# driver.find_element_by_css_selector("#menu-item-40>a").click()
# driver.find_element_by_xpath("//img[@title='Android Quick Start Guide']").click()
# old_price = driver.execute_script("return document.getElementsByClassName('woocommerce-Price-amount')[0].innerText")
# assert old_price == "₹600.00"
# new_price = driver.execute_script("return document.getElementsByClassName('woocommerce-Price-amount')[1].innerText")
# assert new_price == "₹450.00"
# pict_chk = WebDriverWait(driver, 3).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR,(('#product-169>div>a>img'))))
# )
# driver.find_element_by_css_selector("#product-169>div>a>img").click()
# avatar_chk = WebDriverWait(driver, 4).until(
#     EC.element_to_be_clickable((By.ID,(('fullResImage'))))
# )
# driver.find_element_by_class_name("pp_close").click()
# driver.quit()

# Shop проверка цены в корзине

# driver.find_element_by_css_selector("#menu-item-40>a").click()
# Книга HTML5 не доступна к покупке. Выбрал Selenium Ruby
# driver.find_element_by_css_selector("#content>ul>li:nth-child(7)>a:nth-child(2)").click()
# time.sleep(1)
# assert "1 Item" == driver.execute_script("return document.getElementsByClassName('cartcontents')[0].innerText")
# subtot = "₹500.00"
# assert subtot == driver.execute_script("return document.getElementsByClassName('amount')[0].innerText")
# driver.find_element_by_id('wpmenucartli').click()
# subtot_chk = WebDriverWait(driver, 1).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR,(('#page-34>div>div>div>div>table>tbody>tr>td>span'))),subtot)
# )
# tot = "₹525.00"
# tot_chk = WebDriverWait(driver, 3).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR,(('#page-34>div>div>div>div>table>tbody>tr:nth-child(3)>td>strong>span'))),tot)
#  )
# driver.quit()

# Shop Работа в корзине

# driver.find_element_by_css_selector("#menu-item-40>a").click()
# Книга HTML5 не доступна к покупке. Выбрал Selenium Ruby
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector("#content>ul>li:nth-child(7)>a:nth-child(2)").click()
# time.sleep(1)
# Книга не доступна. Выбрал Mastering Java
# driver.find_element_by_css_selector("#content>ul>li:nth-child(6)>a:nth-child(2)").click()
# driver.find_element_by_id('wpmenucartli').click()
# time.sleep(1)
# driver.find_element_by_css_selector("#page-34>div>div>form>table>tbody>tr:nth-child(1)>td>a").click()
# driver.find_element_by_css_selector("#page-34>div>div>div>a").click()
# qnty = "#page-34>div>div>form>table>tbody>tr>td:nth-child(5)>div>input"
# driver.find_element_by_css_selector(qnty).clear()
# driver.find_element_by_css_selector(qnty).send_keys("3")
# driver.find_element_by_css_selector("#page-34>div>div>form>table>tbody>tr:nth-child(3)>td>input:nth-child(2)").click()
# assert "3" == driver.find_element_by_css_selector(qnty).get_attribute("value")
# time.sleep(2)
# driver.find_element_by_css_selector("#page-34>div>div>form>table>tbody>tr:nth-child(3)>td>div>input:nth-child(3)").click()
# msg = driver.find_element_by_css_selector("#page-34>div>div>ul>li")
# msg_chk = WebDriverWait(driver, 3).until_not(
# EC.invisibility_of_element_located(msg)
# )
# driver.quit()

# Shop покупка товара

driver.find_element_by_css_selector("#menu-item-40>a").click()
driver.execute_script("window.scrollBy(0, 300);")
# Книга HTML5 не доступна к покупке. Выбрал Selenium Ruby
driver.find_element_by_css_selector("#content>ul>li:nth-child(7)>a:nth-child(2)").click()
time.sleep(1)
driver.find_element_by_id('wpmenucartli').click()

chkout_btn_chk = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable((By.CLASS_NAME,(("checkout-button"and"button"and"alt"and"wc-forward"))))
 )
driver.find_element_by_class_name("checkout-button"and"button"and"alt"and"wc-forward").click()
# следующий пункт 6
frst_name_chk = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable((By.ID,(("billing_first_name"))))
)
driver.find_element_by_id("billing_first_name").send_keys("Vova")
driver.find_element_by_id("billing_last_name").send_keys("Pupkin")
driver.find_element_by_id("billing_email").send_keys("qqq@mail.ro")
driver.find_element_by_id("billing_phone").send_keys("89219999999")
driver.find_element_by_id("billing_address_1").send_keys("Lenina 8-1-14")
driver.find_element_by_id("billing_city").send_keys("Urypinsk")
driver.find_element_by_id("billing_state").send_keys("Volgogradskaya reg.")
driver.find_element_by_id("billing_postcode").send_keys("123654")

driver.execute_script("window.scrollBy(0, -300);")
driver.execute_script("document.querySelectorAll('#customer_details>div>div>p:nth-child(9)>div>a>span:nth-child(3)').click()")
time.sleep(2)
# count_sel = driver.find_elements_by_class_name("country_to_state")[0]
# count_sel.click()
# time.sleep(10)




# Нужное
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# driver.find_element_by_id("payment_method_cheque").click()
# driver.find_element_by_id("place_order").click()
# txt_chk = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.ID, "content"), "Thank you. Your order has been received.")
# )
# txt_chk = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#page-35>div>div>ul>li:nth-child(4)"), "Check Payments")
# )
# driver.quit()
#
