import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

        # HomePage Elements
        HomePage_obj = Homepage(self.driver)
        HomePage_obj.Menu_Option().click()
        log.info("clicked on menu option ")
        HomePage_obj.Admin_functions().click()
        log.info("Admin funtions")
        time.sleep(2)

        # Announcement elements
        Announcement_obj = Admin_Page(self.driver)
        Announcement_obj.Announcement().click()
        log.info("Clicked on Announcement")
        time.sleep(1)
        Announcement_obj.Edit_Announcement().click()
        log.info("Clicked on Edit announcement")
        time.sleep(2)
        Announcement_obj.New_announcement_name().clear()
        time.sleep(1)
        Announcement_obj.New_announcement_name().send_keys("testing new announcement 2")
        log.info("Entered the new name for Announcement")
        self.driver.execute_script("window.scrollTo({},{});".format(0, 1000))

        Announcement_obj.Click_start_date().click()
        log.info("Clicked on start date")
        #self.driver.find_element_by_xpath("//div[@data-ng-model='announcement.start']//i[@class='glyphicon glyphicon-arrow-right']").click()
        Announcement_obj.Select_new_start_month().click()
        log.info("Selected next month for start date")
        Announcement_obj.New_start_date().click()
        log.info(("Selected new start date"))
        Announcement_obj.Select_time().click()
        log.info("Clicked on start date time")
        Announcement_obj.Select_Precise_time().click()
        log.info("Clicked on start date precise time")
        Announcement_obj.Click_end_date().click()
        log.info("Clicked on End date Calendar")
        Announcement_obj.Select_diff_month().click()
        Announcement_obj.Select_diff_month().click()
        Announcement_obj.Select_diff_month().click()
        Announcement_obj.Select_diff_month().click()
        log.info("Selected different month")
        #Announcement_obj.New_end_date().click()
        Announcement_obj.Select_end_date().click()
        log.info("Select end date")
        Announcement_obj.Select_end_time().click()
        log.info("Select end time")
        Announcement_obj.Select_precise_end_time().click()
        log.info("Select precise end time")
        Announcement_obj.Edit_submit().click()
        time.sleep(2)
        log.info("submitted announcement")
        time.sleep(2)


