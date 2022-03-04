import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from PageObject.Admin_funtions_page import Admin_Page
from PageObject.Attributes import Attributes
from PageObject.HomePage import Homepage
from PageObject.SignInPage import Signin_page
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestFirst(BaseClass):

    def test_push_notification(self):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5)
        log = self.getLogger()
        #Signin Page elements
        Signin_obj = Signin_page(self.driver)
        Signin_obj.signin_path().click()
        log.info("clicked on sign in")
        time.sleep(2)
        Signin_obj.Email_path().send_keys(Signin_page.username_key)
        Signin_obj.Password_path()
        Signin_obj.Sigin_path().click()
        get_title = self.driver.title
        log.info(get_title)
        time.sleep(2)

        # HomePage Elements
        HomePage_obj = Homepage(self.driver)
        HomePage_obj.Menu_Option().click()
        log.info("clicked on menu option ")
        time.sleep(2)
        HomePage_obj.Admin_functions().click()
        log.info("Admin funtions")
        time.sleep(2)

        #Push Notification elements

        Notification_obj = Admin_Page(self.driver)
        Notification_obj.Click_push_notification().click()
        time.sleep(1)
        Notification_obj.Click_organization().click()
        Notification_obj.Click_Department().click()
        Notification_obj.Search_recipient().send_keys('test1@aig.sg')
        time.sleep(2)
        Notification_obj.Search_recipient().send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        Notification_obj.Search_recipient().send_keys(Keys.ENTER)
        type = Notification_obj.Select_Notification_type()
        time.sleep(2)
        type_drop = Select(type)
        type_drop.select_by_visible_text("Survey")
        time.sleep(2)
        Notification_obj.Enter_url().send_keys("https://cerrapoints.com/admin-dashboard/#/push-notification")
        time.sleep(2)
        Notification_obj.Select_notification_image().send_keys("/Users/mac/Desktop/2021-05-30 01.12.12.jpg")
        time.sleep(2)
        Notification_obj.Enter_message().send_keys("TOP RATED (BEST SELLER) #1 Master SELENIUM java course -5 Million students learning worldWide with great collaboration")
        time.sleep(2)

        #Notification_obj.Click_send_notification().click()
        time.sleep(3)
        Notification_obj.Click_confirm_notification().click()
        time.sleep(5)



