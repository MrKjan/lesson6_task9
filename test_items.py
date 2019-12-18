import pytest
import time
from selenium import webdriver

def test_has_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(3)
    try:
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
    except:
        assert button == None, 'Site has no add-to-basket button'