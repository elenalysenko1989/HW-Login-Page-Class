from selenium.webdriver.common.by import By

class  CheckoutPage:


    checkout_button = '#checkout' 

    def __init__(self, driver):
        self.driver = driver

    def click_on_checkout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkout_button).click()