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

        # Announcement elements
        Announcement_obj = Admin_Page(self.driver)
        Announcement_obj.Event_tab().click()
        time.sleep(2)
        Announcement_obj.Click_Create_evemt().click()
        time.sleep(5)
        Announcement_obj.Event_Name().send_keys("testing event 1")
        time.sleep(5)
        Announcement_obj.Event_Department().click()
        time.sleep(5)
        contact_detail = Announcement_obj.Select_contact()
        time.sleep(5)
        contact_detail.click()
        time.sleep(5)
        drop = Select(contact_detail)
        time.sleep(5)
        drop.select_by_visible_text("tester@org.com")
        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='ui-tinymce-3_ifr']"))
        time.sleep(5)
        self.driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("Event Description")
        time.sleep(5)
        self.driver.switch_to.default_content()
        time.sleep(5)
        type_event = Announcement_obj.Event_type()
        time.sleep(5)
        type_event.click()
        time.sleep(5)
        drop_event_type = Select(type_event)
        time.sleep(5)
        drop_event_type.select_by_visible_text("Development")
        time.sleep(5)
        Announcement_obj.Event_Max_Capacity().clear()
        time.sleep(5)
        Announcement_obj.Event_Max_Capacity().send_keys("10")
        time.sleep(5)
        Announcement_obj.Event_Image().send_keys("/Users/mac/Downloads/1 Injasati SS/147,216.jpeg")
        time.sleep(5)
        Announcement_obj.Event_Location().send_keys("Bengaluru, Karnataka, India")
        time.sleep(5)
        time.sleep(2)
        Announcement_obj.Event_Location().send_keys(Keys.ARROW_DOWN)
        time.sleep(5)
        Announcement_obj.Event_Location().send_keys(Keys.ENTER)
        time.sleep(5)
        Announcement_obj.Event_points().clear()
        time.sleep(5)
        Announcement_obj.Event_points().send_keys("10")
        time.sleep(5)
        Announcement_obj.Event_Password().send_keys('pass')
        time.sleep(5)
        Announcement_obj.Click_Event_start().click()

        Announcement_obj.Click_right_arrow().click()

        Announcement_obj.Click_right_arrow().click()

        Announcement_obj.Select_event_start_date().click()
        time.sleep(5)
        Announcement_obj.Select_event_start_time().click()
        time.sleep(5)
        Announcement_obj.Select_event_precise_time().click()
        time.sleep(5)
        Announcement_obj.Click_Event_end().click()
        time.sleep(5)
        Announcement_obj.Click_end_right_arrow().click()
        time.sleep(5)
        Announcement_obj.Click_end_right_arrow().click()
        time.sleep(5)
        Announcement_obj.Click_end_right_arrow().click()
        time.sleep(5)
        Announcement_obj.Click_end_right_arrow().click()
        time.sleep(5)
        Announcement_obj.Select_event_end_date().click()
        time.sleep(5)
        Announcement_obj.Select_event_end_time().click()
        time.sleep(5)
        Announcement_obj.Select_precise_end_time().click()
        time.sleep(5)
        Announcement_obj.Event_RSVP().click()
        time.sleep(5)
        Announcement_obj.RSVP_right().click()
        time.sleep(5)
        Announcement_obj.RSVP_date().click()
        time.sleep(5)
        Announcement_obj.Event_submit().click()

        time.sleep(10)














