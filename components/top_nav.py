from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Top_nav(BasePage):

    DROPDOWN_MENU = (By.CLASS_NAME, "oxd-userdropdown")

    ABOUT_OPTION = (By.CSS_SELECTOR, "a[href='#']")
    SUPPORT_OPTION = (By.CSS_SELECTOR, "a['href=/web/index.php/help/support']")
    CHANGE_PASSWORD_OPTION = (
        By.CSS_SELECTOR,
        "a[href=/web/index.php/pim/updatePassword]",
    )
    LOGOUT_OPTION = (By.CSS_SELECTOR, "a[href='/web/index.php/auth/logout']")

    def select_about_option(self):
        self.click(self.DROPDOWN_MENU)
        self.click(self.ABOUT_OPTION)

    def select_support_option(self):
        self.click(self.DROPDOWN_MENU)
        self.click(self.SUPPORT_OPTION)

    def select_change_password_option(self):
        self.click(self.DROPDOWN_MENU)
        self.click(self.CHANGE_PASSWORD_OPTION)

    def select_logout_option(self):
        self.click(self.DROPDOWN_MENU)
        self.click(self.LOGOUT_OPTION)
