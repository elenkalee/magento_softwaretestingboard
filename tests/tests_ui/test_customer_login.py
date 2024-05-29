from pages.CustomerLoginPage import CustomerLoginPage


class TestCustomerLoginPage:

    def test_browser_title_of_direct_link_to_customer_login_page(self, browser):
        """ Check if the browser title for direct link of Customer Login Page is Customer Login """
        sign_in_page = CustomerLoginPage(browser)
        sign_in_page.go_to_page()
        # TODO: Here it takes URL from properties of Customer Login Page, how to use base url + endpoint
        assert browser.title == "Customer Login"

    # DRAFT:
    # def test_check_customer_login_with_correct_credentials(self, browser):
    #     sign_in_page = CustomerLoginPage(browser)
    #     sign_in_page.go_to_page()
    #     sign_in_page.fill_in_email_input()

