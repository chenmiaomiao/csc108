# _*_ coding: utf8 _*_

from selenium import webdriver
import time

# driver = webdriver.Ie()

driver = webdriver.Chrome()

driver.get('https://cas.csc108.com/login?service=http%3A%2F%2Ftzgw.csc108.com%3A8080%2Fj_spring_cas_security_check%3Bjsessionid%3Dvpq3XMWLbbhQybkrr3TNqWyn8Q9CPQGh45qt1Y5PgKzt3hvJBkfH%211663513085')

#new_account = driver.find_element_by_xpath("//div[@class='newleft']/table/tbody/tr/td[@height='200']/label")

#new_account = driver.find_element_by_partial_link_text('新开户请点击')

time.sleep(1)

new_account = driver.find_element_by_xpath("//input[@id='username']") 

new_account.send_keys('lirm')

