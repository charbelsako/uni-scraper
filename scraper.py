from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# SAFELY READ YOUR PASSWORD WITHOUT ANYONE SEEING IT
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

username = config['SECRET']['USERNAME']
password = config['SECRET']['PASSWORD']
# start chrome
browser = webdriver.Chrome()
# navigate to your url
url = 'http://elearning.aut.edu/course/view.php?id=1548'
browser.get((url))

# fill in username
usernameInput = browser.find_element_by_id('username')
usernameInput.send_keys(username)
# fill in your password
passwordInput = browser.find_element_by_id('password')
passwordInput.send_keys(password)
# click the login button
loginButton = browser.find_element_by_id('loginbtn')
loginButton.click()
# Do more stuff
# you might want to wait the new page to load