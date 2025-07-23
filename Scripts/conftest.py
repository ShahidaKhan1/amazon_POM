import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture()
def browser_setup():
    driver = webdriver.Chrome(opts)
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()