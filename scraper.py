from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# num_courses = int(input('Enter the number of courses you are registered in: '))

# get the course list
def get_course_list():
  browser.implicitly_wait(3) # wait for three seconds
  return browser.find_elements_by_css_selector('li.type_course.depth_3 > p > a')

# if there is a summary div click on the link in that.
# then get all the files and click on each one. Not all of them will download.
# some of them are pdfs so they open up in a new tab.  
def download_course_content():
  # Gets the links for all of the content.
  files = browser.find_elements_by_css_selector('.activityinstance > a')
  links = [files for file in files if 'resource' in file.get_attribute('href')]
  print(len(links))
  # if 'resource' in links[?]
  # check if link is a resource before clicking on it.

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

loginButton = browser.find_element_by_id('loginbtn') # get the login button
loginButton.click() # click the login button.

browser.implicitly_wait(5) # wait for (5 seconds) the page to load

course_list = get_course_list() # Get the links of all courses 
for i in range(len(course_list)):
  course_list[i].click()
  browser.implicitly_wait(3)
  download_course_content()
  browser.back() # goes to the previous page.
  browser.implicitly_wait(3) 
  course_list = get_course_list()