from pages.BasePage import BasePage


class CustomerLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = ("https://magento.softwaretestingboard.com/customer/account/login/referer"
                         "/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
    # TODO: ??? Here I hardcoded the direct link for Customer Login Page. But if I want to write tests for direct
    #  links and from Home page -> Sign in link how it should be realized?

    """Customer Login Page actions methods come here"""

    # def fill_in_email_input(self):
    #     self._input_fill(CustomerLoginPageLocators.EMAIL_ADDRESS_INPUT, 'elena.42rus@yandex.ru')
    #     # TODO: How to connect env and credentials

    # def fill_in_password_input(self):
    #     pass
    #
    # def click_on_sign_in_button(self):
    #     return self.driver.find_element(CustomerLoginPageLocators.SIGNIN_BUTTON, time=2).click()
    #
    # def click_to_forgot_your_password_link(self):
    #     pass
    #
    # def click_on_create_an_account(self):
    #     # TODO: How is better to call methods if the same actions from different places
    #     pass

