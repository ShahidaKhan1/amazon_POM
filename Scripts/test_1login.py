import sys
import os

# Add parent directory to path to allow imports
sys.path.append(os.path.abspath(".."))

from POM.login import Login
from generic_utilities.excel_utility import excel_data

data = excel_data('Sheet1')

def test_login(browser_setup):
    login_obj = Login(browser_setup)
    login_obj.click_on_login()
    login_obj.enter_login_email(data['login_email'])
    login_obj.click_continue()
    login_obj.enter_login_pwd(data['login_pwd'])
    login_obj.click_signin()