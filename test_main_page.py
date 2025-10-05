import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_items(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(10)
    time.sleep(5)
    elems = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(elems) == 1, 'Элемент не найден' if len(elems) == 0 else 'Найдено несколько элементов'