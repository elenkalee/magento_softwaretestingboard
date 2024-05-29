from pages.HomePage import HomePage


class TestHomePage:
    def test_home_page_title(self, browser):
        """Check if browser title is Home Page"""
        home_page = HomePage(browser)
        home_page.go_to_page()
        assert browser.title == "Home Page"
