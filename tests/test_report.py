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

        # Admin Report Elements

        self.driver.execute_script("window.scrollTo(0, 4000)")
        time.sleep(2)
        Reports_obj = Admin_Page(self.driver)
        x = Reports_obj.Report_Download()
        time.sleep(2)
        drop = Select(x)
        drop.select_by_visible_text("Users")
        time.sleep(2)

        y = Reports_obj.Filter_by()
        drop2 = Select(y)
        drop2.select_by_visible_text("Overall")
        time.sleep(2)

        Reports_obj.Export_CSV().click()
        time.sleep(5)
        Reports_obj.Download_CSV().click()










