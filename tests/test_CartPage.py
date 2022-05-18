from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.ProductDetailsPage import ProductDetailsPage
from pages.ProductListPage import ProductListPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger
from selenium.webdriver.common.by import By

class TestProdDetails:

    logger =Logger.get_logger()

    def test_click_on_cart_icon(self, setup):
        self.logger.info('********** Test Case: Go back to Products from Product Details')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.view_product_details()
      

        self.logger.info('Product is added')
    
        self.click_on_cart_icon_page = CartPage(self.driver)
        self.click_on_cart_icon_page.click_on_cart_icon()
        if 'description' in self.driver.page_source.lower():
            assert True
        else:
            assert False
    