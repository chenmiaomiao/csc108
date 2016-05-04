# _*_ coding: utf8 _*_

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.keys import Keys
import time

def save_shot(name, bin_image):
    current_time = time.time()
    fhand = open(name + str(current_time) + '.png', 'wb')
    fhand.write(bin_image)
    fhand.close()
    
def take_shot_(driver):
    name = 'shot'
    bin_image = driver.get_screenshot_as_png()
    save_shot(name, bin_image)
    
    print 'Screenshot had been taken. '

class NewAccount():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
        # self.driver = webdriver.Ie()
    
    def go_to_login_page(self):        
        self.driver.get('https://account.csc108.com/index/main.jspx')
        
        # switch to frame
        # iframe_step = driver.find_element_by_xpath("//iframe[@class='step']") 
        # driver.switch_to_frame(iframe_step)
        
        # jump to account opening page
            
        # go_to_new_account_page = driver.find_element_by_xpath("//div[@id='nex']")
        
        go_to_new_account_page = self.driver.find_element_by_xpath("//div[@class='pagingg_right']")
        
        print go_to_new_account_page
        
        # go_to_new_account_page.send_keys(Keys.ENTER)
        
        go_to_new_account_page.click()
        
        # 
        
        take_shot_(self.driver)
        
        print 'Eureka! '
            
    def find_department(self):
        
        iframe_account_main = self.driver.find_element_by_id('account_main_iframe')
        
        self.driver.switch_to_frame(iframe_account_main)
        
        iframe_steps_account = self.driver.find_element_by_class_name('step_account_noshadow')
        
        self.driver.switch_to_frame(iframe_steps_account)
        
        suggest_address = self.driver.find_element_by_id('suggestAddress')
        
        suggest_address.clear()
        
        suggest_address.send_keys(u'泸州')
        
        button_search_department = self.driver.find_element_by_xpath("//ul[@class='search_department']/li[@class='button']")
        
        button_search_department.click()
        
        
        take_shot_(self.driver)
        
        button_open = self.driver.find_element_by_class_name('openbutton')
        
        button_open.click()
        
        
        take_shot_(self.driver)
    
    def driver_quit(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    new_account = NewAccount()
    new_account.go_to_login_page()
    new_account.find_department()
    quit_if = raw_input('Quit? (y/n)')
    if quit_if.upper() == 'Y':
        new_account.driver_quit()