import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"

class BasePage():
   def __init__(self, browser, url):
      self.browser = browser
      self.url = url
    
   def open(self):
      self.browser.get(self.url)                                 
 