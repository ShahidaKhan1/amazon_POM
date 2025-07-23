from object_repository.search_page_repo import SearchedProductLocators

searched_loc = SearchedProductLocators()

class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def select_first_result(self):
        self.driver.find_element(*searched_loc.product_searched).click()

