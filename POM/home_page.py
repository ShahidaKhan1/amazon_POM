from object_repository.homepage_repo import HomepageLocators

homepage_loc = HomepageLocators()

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver

        # Search and click book
    def search_product(self, product_name):
        self.search_box = self.driver.find_element(*homepage_loc.product).send_keys(product_name)
        
    def search_button(self):
        self.search_click = self.driver.find_element(*homepage_loc.button_search).click()
