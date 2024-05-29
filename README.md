Introduction
------------
**(DRAFT VERSION)**

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium) 

Files
-----
* **[pages](pages)** - The directory which contains all pages of the website
* **[tests](tests)** - The folder with all tests of the project
  * **[tests/tests_api](tests/tests_api)** - API tests for https://softwaretestingboard.com/practice-api-testing-using-magento-2/
  * **[tests/tests_ui](tests/tests_ui)** - UI tests for website https://magento.softwaretestingboard.com/
* **[conftest.py](conftest.py)** - The file contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.
* **[pytest.ini](pytest.ini)** - The configuration file is used to define custom tokens and integrate with plugins and extensions.
* **[.env](.env)** - File with credentials for different environments

How To Run Tests
----------------
1. Copy the repository
2. Install all requirements:

    ```bash
    python -m pip install -r requirements.txt
    ```

3. Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)
4. Run tests (_now FF is by default_):

    ```bash
    pytest
    ```

Note:
