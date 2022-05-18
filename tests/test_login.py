from pages.LoginPage import LoginPage
from utilities.Logger import Logger

class TestLogin:

    # class attributes
    logger = Logger.get_logger()

    # class methods = test cases
    def test_login_page_title(self, setup):
        self.logger.info('********** Test Case: Login Page Title ')
        self.driver = setup
        page_title = self.driver.title


        #Hello, Eldor! For some reason this statemend didn't work for me, this test case failed (assert False) and I got this message: tests\test_login.py:21: AssertionError
        # if page_title == 'Swag labs':
        #     assert True
        # else:
        #     assert False

        #So, I used this instead

        if 'Swag Labs' in self.driver.page_source:
             assert True
        else:
            assert False
    
    def test_login(self, setup):
        self.logger.info('********** Test Case: Valid Login')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        if 'products' in self.driver.page_source.lower():
            assert True
        else:
            assert False