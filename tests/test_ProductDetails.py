from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.ProductDetailsPage import ProductDetailsPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger
from selenium.webdriver.common.by import By

class TestProdDetails:

    logger =Logger.get_logger()
    def test_back_to_products(self, setup):
        self.logger.info('********** Test Case: Go back to Products from Product Details')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.view_product_details()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.back_to_products()
        if 'back to products' in self.driver.page_source.lower():
             assert True
        else:
            assert False