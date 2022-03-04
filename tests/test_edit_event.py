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

    def test_point_allocation(self):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5)
        log = self.getLogger()
        #Signin Page elements
        Signin_obj = Signin_page(self.driver)
        Signin_obj.signin_path().click()
        log.info("clicked on sign in")
        time.sleep(5)
        Signin_obj.Email_path().send_keys(Signin_page.username_key)
        Signin_obj.Password_path()
        Signin_obj.Sigin_path().click()
        get_title = self.driver.title
        log.info(get_title)
        time.sleep(4)

        # HomePage Elements
        HomePage_obj = Homepage(self.driver)
        HomePage_obj.Menu_Option().click()
        log.info("clicked on menu option ")
        time.sleep(2)
        HomePage_obj.Admin_functions().click()
        log.info("Admin funtions")
        time.sleep(2)

        # Announcement elements
        Announcement_obj = Admin_Page(self.driver)
        time.sleep(3)
        Announcement_obj.Event_tab().click()
        time.sleep(3)
        Announcement_obj.Edit_Event().click()
        log.info("clicked on edit")
        time.sleep(2)
        Announcement_obj.New_Event_Name().clear()
        time.sleep(3)
        Announcement_obj.New_Event_Name().send_keys('testing new event 1')
        log.info("Changed the event name")
        time.sleep(3)
        Announcement_obj.Event_points().clear()
        log.info("Cleared the event point")
        time.sleep(3)
        Announcement_obj.Event_points().send_keys("5")
        log.info("Entered new keys")
        time.sleep(3)
        Announcement_obj.Click_Event_start().click()
        Announcement_obj.Click_right_arrow().click()
        Announcement_obj.Click_right_arrow().click()
        Announcement_obj.Click_right_arrow().click()
        time.sleep(3)
        Announcement_obj.Select_event_start_date().click()
        Announcement_obj.Select_event_start_time().click()
        Announcement_obj.Select_event_precise_time().click()
        time.sleep(3)
        Announcement_obj.Click_Event_end().click()
        time.sleep(3)
        Announcement_obj.Click_end_right_arrow().click()
        Announcement_obj.Click_end_right_arrow().click()
        Announcement_obj.Click_end_right_arrow().click()
        Announcement_obj.Click_end_right_arrow().click()
        Announcement_obj.Click_end_right_arrow().click()
        Announcement_obj.Select_event_end_date().click()
        Announcement_obj.Select_event_end_time().click()
        time.sleep(3)
        Announcement_obj.Select_precise_end_time().click()
        time.sleep(3)
        Announcement_obj.Event_submit().click()
        time.sleep(3)