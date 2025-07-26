from object_repository.homepage_repo import HomepageLocators

homepage_loc = HomepageLocators()

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver

    # Search book
    def search_product(self, product_name):
        self.driver.find_element(*homepage_loc.product).send_keys(product_name)

    #click on the search icon 
    def search_button(self):
        self.driver.find_element(*homepage_loc.button_search).click()

    #click on first result
    def select_first_result(self):
        self.driver.find_element(*homepage_loc.product_searched).click()
    
    # Add to cart
    def add_to_cart(self):
        self.driver.find_element(*homepage_loc.add_to_cart_button).click()

    # click on cart
    def click_on_cart(self):
        self.driver.find_element(*homepage_loc.click_on_cart).click()

    # click on proceed to buy
    def click_proceed_to_buy(self):
        self.driver.find_element(*homepage_loc.proceed_to_buy_button).click()
