import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.Admin_funtions_page import Admin_Page
from PageObject.HomePage import Homepage
from PageObject.SignInPage import Signin_page
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestFirst(BaseClass):

    def test_bulk_point_allocation(self):
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
        time.sleep(2)
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
        Allocate_points_obj.Bulk_pointallocation().click()
        log.info("Clicked on bulk point allocation")
        time.sleep(3)
        point_upload = Allocate_points_obj.Choose_file()
        point_upload.send_keys("/Users/mac/Desktop/bulk_point_upload.xlsx")
        time.sleep(3)
        Allocate_points_obj.Send_email().click()
        time.sleep(3)
        Allocate_points_obj.Send_push().click()
        time.sleep(3)
        Allocate_points_obj.Submit().click()
        time.sleep(5)

        #alog.info("Successfully uploaded")
