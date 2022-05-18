from selenium.webdriver.common.by import By

class  CartPage:


    cart_icon = '.shopping_cart_link' 

    def __init__(self, driver):
        self.driver = driver

   


    def click_on_cart_icon(self):
         self.driver.find_element(By.CSS_SELECTOR, self.cart_icon).click()
    