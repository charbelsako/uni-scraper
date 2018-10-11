from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# SAFELY READ YOUR PASSWORD WITHOUT ANYONE SEEING IT
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

username = config['SECRET']['USERNAME']
password = config['SECRET']['PASSWORD']
# start chrome
browser = webdriver.Chrome()
# navigate to your url
url = 'http://elearning.aut.edu/my/'
browser.get(url)

# fill in username
usernameInput = browser.find_element_by_id('username')
usernameInput.send_keys(username)
# fill in your password
passwordInput = browser.find_element_by_id('password')
passwordInput.send_keys(password)
# click the login button.
loginButton = browser.find_element_by_id('loginbtn')
loginButton.click()
# Get the links of all courses
browser.implicitly_wait(5)
# this works
# course_list =  browser.find_elements_by_css_selector('li.type_course.depth_3')
course_list =  browser.find_elements_by_css_selector('li.type_course.depth_3 > p > a')

#if I click I lose my links. Or do I?
course_list[0].click()
browser.implicitly_wait(5)
course_list[1].click()