from selenium.webdriver.common.by import By

class ProductDetailsPage:

    
    button_back_to_products_css = '#back-to-products'

    
    def __init__(self, driver):
        self.driver = driver
    
    
    def back_to_products(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_back_to_products_css)