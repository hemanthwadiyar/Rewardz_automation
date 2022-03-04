import pytest
from selenium import webdriver
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

    def test_point_allocation(self):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5)
        log = self.getLogger()
        #Signin Page elements
        Signin_obj = Signin_page(self.driver)
        Signin_obj.signin_path().click()
        log.info("clicked on sign in")
        Signin_obj.Email_path().send_keys(Signin_page.username_key)
        Signin_obj.Password_path()
        Signin_obj.Sigin_path().click()
        get_title = self.driver.title
        log.info(get_title)
        time.sleep(3)

        #HomePage Elements
        HomePage_obj = Homepage(self.driver)
        HomePage_obj.Menu_Option().click()
        log.info("clicked on menu option ")
        time.sleep(3)
        HomePage_obj.Admin_functions().click()
        log.info("Admin funtions")
        time.sleep(2)

        # Allocate points elements
        Allocate_points_obj = Admin_Page(self.driver)
        Allocate_points_obj.allocate_point().click()
        log.info("Clicked on Allocate points")
        time.sleep(3)
        Allocate_points_obj.Transaction_History().click()
        log.info("Clicked on transaction history")
        time.sleep(3)
        Allocate_points_obj.Click_Edit_points().click()
        log.info("Click edit points")
        time.sleep(2)
        Allocate_points_obj.Change_points().click()
        log.info("clicked on points tab")
        time.sleep(3)
        Allocate_points_obj.Change_points().clear()
        log.info("Cleared points")
        time.sleep(3)
        Allocate_points_obj.Change_points().send_keys("20")
        log.info("Entered new points")
        time.sleep(3)
        Allocate_points_obj.Click_Update().click()
        log.info("Clicked on update")
        time.sleep(10)

