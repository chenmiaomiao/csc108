# _*_ coding: utf8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Ie()

# driver = webdriver.Chrome()


def go_to_login_page():
    driver.get('https://account.csc108.com/index/main.jspx?t_=1461646494789')
    
    # switch to frame
    iframe_step = driver.find_element_by_xpath("//iframe[@class='step']") 
    driver.switch_to_frame(iframe_step)
    
    # jump to account opening page
    new_account = driver.find_element_by_xpath("//div[@class='newleft']")
    
    print new_account
    
    new_account.click()
    # new_account.click()
    
    print 'Eureka! '

if __name__ == '__main__':
    go_to_login_page()