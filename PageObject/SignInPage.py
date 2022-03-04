
from selenium.webdriver.common.by import By

from PageObject.Attributes import Attributes

class Signin_page(Attributes):

    def __init__(self, driver):
        self.driver = driver

    def signin_path(self):
        return self.driver.find_element(*Attributes.login_button)

    def Email_path(self):
        return self.driver.find_element(*Attributes.email_text_field)

    def Password_path(self):
        return self.driver.find_element(*Attributes.password).send_keys(*Attributes.password_key)

    def Sigin_path(self):
        return self.driver.find_element(*Attributes.click_to_signin)



