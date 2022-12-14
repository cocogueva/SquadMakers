from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    TXT_USERNAME = (By.ID, "user-name")
    TXT_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")

    HAMBURGER = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
            super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
            self.input_element(self.TXT_USERNAME, user)
            self.input_element(self.TXT_PASSWORD, pwd)

    def enter_login(self):
            self.click_element(self.BTN_LOGIN)

    def log_out(self):
        self.click_element(self.HAMBURGER)
        self.click_element(self.LOGOUT)