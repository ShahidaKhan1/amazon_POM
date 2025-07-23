class LoginLocators:

    def __init__(self):
        self.login_button = ('xpath','(//a[@data-nav-role="signin"])[1]')
        self.login_email = ('xpath', '//input[@name="email"]')
        self.continue_button = ('xpath', '(//span[@class="a-button-inner"])[2]')
        self.login_pwd = ('xpath', '//input[@id="ap_password"]')
        self.signin = ('xpath', '(//span[@class="a-button-inner"])[1]')
