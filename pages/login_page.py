from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    path = "web/index.php/auth/login"

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REQUIRED_FIELD_ERROR = (
        By.CSS_SELECTOR,
        ".oxd-input-group__message",
    )
    INVALID_CREDENTIALS_ERROR = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

    def navigate(self):
        self.open(self.path)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
