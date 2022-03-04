from selenium.webdriver.common.by import By

#from pageObjects.CheckoutPage import CheckOutPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@placeholder='Email or username']")
    password = (By.XPATH, "//input[@type='password']")
    signin = (By.XPATH, "//button[contains(text(),'Sign In')]")
    forgotpassword = (By.XPATH, "//a[contains(text(),'Forgot Your Password')]")
    close = (By.XPATH, "//div[@id='myModal']//div[@class='modal-dialog']//div[@class='modal-content']//div[@class='modal-header']//button[@type='button']//span[@aria-hidden='true'][contains(text(),'×')]")
    alert = (By.XPATH,"//div[@class='alert alert-danger']")



    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickSignin(self):
        return self.driver.find_element(*LoginPage.signin)

    def clickForgotPassword(self):
        return self.driver.find_element(*LoginPage.forgotpassword)

    def clickClose(self):
        return self.driver.find_element(*LoginPage.close)

    def getAlertMessage(self):
        return self.driver.find_element(*LoginPage.alert)




