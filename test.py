from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wd = webdriver.Chrome()
wd.get('https://www.baidu.com')

kuang = wd.find_element_by_id("kw")
kuang.send_keys('asdf' + Keys.RETURN)
kuang = wd.find_element_by_class_name("result c-container ")
print(kuang)
print('asdf')