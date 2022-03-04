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
        time.sleep(5)
        HomePage_obj.Admin_functions().click()
        log.info("Admin funtions")
        time.sleep(2)

        # Announcement elements
        Announcement_obj = Admin_Page(self.driver)
        Announcement_obj.Announcement().click()
        log.info("Clicked on Announcement")
        time.sleep(1)
        Announcement_obj.Create_Announcement().click()
        log.info("clicked on create announcement")
        Announcement_obj.Announcement_name().send_keys("testing announcement 3")
        time.sleep(2)
        log.info("Entered the name for Announcement")
        Announcement_obj.Select_ann_department().click()
        time.sleep(2)
        log.info("Selected the department for Announcement")
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='ui-tinymce-2_ifr']"))
        time.sleep(2)
        self.driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("Entering Description")
        time.sleep(2)
        self.driver.switch_to_default_content()
        time.sleep(1)
        Announcement_obj.Select_image().send_keys("/Users/mac/Downloads/1 Injasati SS/164,196.jpeg")
        log.info("Selected the image for Announcement")
        time.sleep(2)
        Announcement_obj.Select_file().send_keys("/Users/mac/Desktop/2021-05-30 01.12.12.jpg")
        log.info("Selected the file for Announcement")
        time.sleep(2)
        Announcement_obj.Give_URL().send_keys("https://canvas.instructure.com/courses/2412303")
        log.info("Provided the URL for Announcement")
        time.sleep(2)
        Announcement_obj.Click_start_date().click()
        log.info("Clicked on start date")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@data-ng-model='announcement.start']//i[@class='glyphicon glyphicon-arrow-right']").click()
        Announcement_obj.Select_start_date().click()
        log.info("Clicked on start date")
        time.sleep(2)
        Announcement_obj.Select_time().click()
        log.info("Clicked on start date time")
        time.sleep(2)
        Announcement_obj.Select_Precise_time().click()
        log.info("Clicked on start date precise time")
        time.sleep(2)
        Announcement_obj.Click_end_date().click()
        log.info("Clicked on End date Calendar")
        time.sleep(2)
        Announcement_obj.Select_diff_month().click()
        Announcement_obj.Select_diff_month().click()
        Announcement_obj.Select_diff_month().click()
        Announcement_obj.Select_diff_month().click()
        log.info("Selected different month")
        time.sleep(2)
        Announcement_obj.Select_end_date().click()
        log.info("Select end date")
        time.sleep(2)
        Announcement_obj.Select_end_time().click()
        log.info("Select end time")
        Announcement_obj.Select_precise_end_time().click()
        log.info("Select precise end time")

        Announcement_obj.Select_is_priority().click()
        log.info("Selected is priority")
        time.sleep(2)
        Announcement_obj.Click_Ann_submit()
        time.sleep(2)
        log.info("submitted announcement")
        time.sleep(3)









