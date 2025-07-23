from object_repository.login_repo import LoginLocators

login_loc = LoginLocators()

class Login:

    def __init__(self, driver):
        self.driver = driver

        # Sign in
    def click_on_login(self):
        self.driver.find_element(*login_loc.login_button).click()
        
    def enter_login_email(self, login_email):
        self.driver.find_element(*login_loc.login_email).send_keys(login_email)
        
    def click_continue(self):
        self.driver.find_element(*login_loc.continue_button).click()

    def enter_login_pwd(self, login_pwd):   
        self.driver.find_element(*login_loc.login_pwd).send_keys(login_pwd)
        
    def click_signin(self):    
        self.driver.find_element(*login_loc.signin).click()
