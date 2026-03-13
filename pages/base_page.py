from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.TIMEOUT)
        self.base_url = Config.BASE_URL

    def open(self, path):
        self.driver.get(f"{self.base_url}{path}")

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def back(self):
        self.driver.back()
