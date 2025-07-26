import time
import sys
import os

# Add parent directory to path to allow imports
sys.path.append(os.path.abspath(".."))

from POM.home_page import HomePage
from generic_utilities.excel_utility import excel_data

data = excel_data('Product_Sheet')

def test_homepage(browser_setup):
    homepage_obj = HomePage(browser_setup)
    homepage_obj.search_product(data['prod1'])
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
