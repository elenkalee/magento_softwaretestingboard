from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://magento.softwaretestingboard.com"
        # TODO: ??? Don't understand how to use url from .env
        """Base class to initialize the base page that will be called from all pages"""

    def go_to_page(self):
        return self.driver.get(self.base_url)

    # DRAFTS:
    # def _verify_element_visibility(self, locator, time=2):
    #     return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f"Element by locator: {locator} NOT found",)
    #
    # def _find_and_click_element(self, locator):
    #     element = self._verify_element_visibility(locator)
    #     element.click()
    #
    # def _input_fill(self, input_field, text):
    #     field = self._verify_element_visibility(input_field)
    #     field.click()
    #     field.clear()
    #     field.send_keys(text)
