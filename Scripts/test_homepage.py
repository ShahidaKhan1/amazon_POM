import time
import sys
import os
# import pytest


# Add parent directory to path to allow imports
sys.path.append(os.path.abspath(".."))

from POM.login import Login
from POM.home_page import HomePage
from generic_utilities.excel_utility import excel_data

login_data = excel_data('Sheet1')
product_data = excel_data('Product_Sheet')


def test_login_and_homepage(browser_setup):

    #Step 1: Login
    login_obj = Login(browser_setup)
    login_obj.click_on_login()
    login_obj.enter_login_email(login_data['login_email'])
    login_obj.click_continue()
    login_obj.enter_login_pwd(login_data['login_pwd'])
    login_obj.click_signin()
    time.sleep(3)

    # Step 2: Home Page actions
    homepage_obj = HomePage(browser_setup)
    homepage_obj.search_product(product_data['prod1'])
    time.sleep(2)
    homepage_obj.search_button()
    time.sleep(2)
    homepage_obj.select_first_result()
    time.sleep(2)
    homepage_obj.add_to_cart()
    time.sleep(2)
    homepage_obj.click_on_cart()
    time.sleep(2)
    homepage_obj.click_proceed_to_buy()
    time.sleep(4)
