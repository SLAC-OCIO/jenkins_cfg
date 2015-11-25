from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

import sys
import unittest

selenium_grid_url="http://134.79.129.233:4444/wd/hub"

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Remote("http://134.79.129.233:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX.copy())
driver.get("http://www.google.com")
driver.get_screenshot_as_file('/Screenshots/google.png')
display.stop()
