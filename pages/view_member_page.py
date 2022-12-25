from time import sleep
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class ViewMemebr(BaseDriver):
    # Locator
    email = (By.ID, 'email')

    def verify_field_after_search(self):
        email = self.driver.find_element(self.email).text
        return email
