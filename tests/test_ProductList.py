from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger

class TestProductListPage:
    logger =Logger.get_logger()
    # def test_text_is_displayed(self, setup):
    #     self.driver = setup
    #     self.login_page = LoginPage(self.driver)
    #     self.logger.info('Login with valid credentials')
    #     self.login_page.valid_login()
    #     self.logger.info('Finding the element Sauce Labs Backpack')
    #     self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    #     self.test_text_is_displayed = ProductListPage(self.driver)
    #     text = self.driver.text
    #     self.logger.info('******Test Case: Text Products is displayed')
    #     if 'Sauce Labs Backpack'.lower() in self.driver.page_source.lower():
    #          assert True
    #     else:
    #         assert False
    def test_add_to_cart(self, setup):
        self.logger.info('********** Test Case: Add to Cart')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        if self.product_list_page.product_added():
            assert True
        else:
            assert False
    
    def test_view_produc_details(self, setup):
        self.logger.info('********** Test Case: View Product Details')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.view_product_details()
        if 'back to products' in self.driver.page_source.lower():
            assert True
        else:
            assert False


