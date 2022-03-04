from PageObject.Attributes import Attributes


class Homepage(Attributes):

    def __init__(self,driver):
        self.driver = driver

    def Menu_Option(self):
        return self.driver.find_element(*Attributes.click_on_menu)

    def Admin_functions(self):
        return self.driver.find_element(*Attributes.click_admin_fun)