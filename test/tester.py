#coding=utf-8

#使用ID定位
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id("kw").send_keys(u"中国selenium")
#通过id定位输入框，html规定，id在文档中必须唯一，类似于我们的身份证号
#driver.find_element_by_id("su").click()
#driver.quit()