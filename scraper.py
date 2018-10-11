import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# options to be able to download pdf files
options = webdriver.ChromeOptions()
download_folder = "C:\\Users\\sarkis\\Desktop\\bot test"    
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], 
"download.default_directory": download_folder,
"download.extensions_to_open": ""}
options.add_experimental_option("prefs", profile)

# gets the course list.
def get_course_list():
  browser.implicitly_wait(3) # wait for three seconds
  return browser.find_elements_by_css_selector('li.type_course.depth_3 > p > a')

# downloads the course content.  
def download_course_content():
  # Gets the links for all of the content.
  files = browser.find_elements_by_css_selector('.activityinstance > a')
  links = [file.get_attribute('href') for file in files]
  file_types = browser.find_elements_by_css_selector('.iconlarge')
  ftypes = []
  
  for file_type in file_types:
    src = file_type.get_attribute('src')
    if 'pdf' not in src:
      ftypes.append('pdf')
    elif 'document' in src:
      ftypes.append('document')
    elif 'forum' in src:
      ftypes.append('forum')
    elif 'attendance' in src:
      ftypes.append('attendance')
    elif 'spreadsheet' in src:
      ftypes.append('spreadsheet')
    elif 'text' in src:
      ftypes.append('text')
    elif 'powerpoint' in src:
      ftypes.append('powerpoint')

  # Iterate over the links
  for i in range(len(files)):
    # TO-DO: check if file already exists.
    if ftypes[i] is not 'forum' and ftypes[i] is not 'text':
      browser.get(links[i])

# SAFELY READ YOUR PASSWORD WITHOUT ANYONE SEEING IT
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
username = config['SECRET']['USERNAME']
password = config['SECRET']['PASSWORD']

browser = webdriver.Chrome(chrome_options = options) # start chrome
url = 'http://elearning.aut.edu/my/'
browser.get(url) # navigate to your url

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
  course_list[i].click() # click on each course link
  browser.implicitly_wait(3) # wait for 3 seconds
  download_course_content() # download important content.
  browser.back() # go back to the previous page.
  browser.implicitly_wait(3) # wait for 3 seconds
  course_list = get_course_list() # get the course list again. Because it disappears after clicking on links
  