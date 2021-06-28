import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.command import Command
import http.client
import socket


def run():
    chromeOptions = Options()
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
    driver.implicitly_wait(15)
    driver.get('https://google.com/')
    writeSession(driver)
    print('Finished Initiating Chrome')

def writeSession(driver):
    url = driver.command_executor._url
    session_id = driver.session_id
    f = open("sessioninfo.txt", "w")
    f.write(f"{url}\n")
    f.write(f"{session_id}")
    f.close()
    print('Wrote webdriver session details')

class Scraper():
    def __init__(self):
      self.driver = attachToSession()

    def getGithub(self):
      try:
        driver = self.driver
        driver.get('https://github.com/')
        print('Sleeping..')
        time.sleep(2)
        print('Sleep done..')
        return 200
      except Exception as e:
        print(e)
        raise e
    
    def getStackOverflow(self):
      try:
        driver = self.driver
        driver.get('https://stackoverflow.com')
        print('Sleeping..')
        time.sleep(2)
        print('Sleep done..')
        return 200
      except Exception as e:
        print(e)
        raise e



def attachToSession():
    # Code Reference : https://stackoverflow.com/a/48194907/11217153
    # The stackover flow answer was adapted. 
    f = open("sessioninfo.txt", "r")
    lines = f.readlines()
    url = lines[0]
    session_id = lines[1]
    session_id.strip()
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver
