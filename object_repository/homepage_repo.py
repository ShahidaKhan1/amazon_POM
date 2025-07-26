class HomepageLocators:

    def __init__(self):
        self.product = ('xpath', '//input[@id="twotabsearchtextbox"]')
        self.button_search = ('xpath','//div[@id="sac-suggestion-row-1"]')
        self.product_searched = ('xpath', '//h2[@aria-label="MINDSET (REVISED AND UPDATED)"]')
        self.add_to_cart_button = ('xpath', '//input[@id="add-to-cart-button"]')
        self.click_on_cart = ('xpath', '//span[@id="nav-cart-count"]')
        self.proceed_to_buy_button = ('xpath', '//input[@name="proceedToRetailCheckout"]')