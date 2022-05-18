
from selenium.webdriver.common.by import By

class  ProductListPage:



    button_inventory_css = '.btn_inventory'
    text_cart_counter_css = '.shopping_cart_badge'
    text_inventory_item_name_css = '.inventory_item_name'

   
    def __init__(self, driver):
        self.driver = driver
    
    
    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_inventory_css).click()
    
    def product_added(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_cart_counter_css).text == '1'
    
    def view_product_details(self):
        product_names = self.driver.find_elements(By.CSS_SELECTOR, self.text_inventory_item_name_css)
        product_names[0].click()

        
      