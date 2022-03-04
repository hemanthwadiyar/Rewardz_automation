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
        Department_dropdown = Allocate_points_obj.Select_department()
        drop = Select(Department_dropdown)
        log.info("Selected department")

        drop.select_by_visible_text(Attributes.department_value)

        User = Allocate_points_obj.Select_user()

        User_dropdown = Select(User)

        User_dropdown.select_by_visible_text(Attributes.User_selection)

        point_category = Allocate_points_obj.Select_category()

        Category_dropdown = Select(point_category)

        Category_dropdown.select_by_visible_text(Attributes.Category_value)

        point_subcategory = Allocate_points_obj.Select_SubCategory()

        Subcategory_dropdown = Select(point_subcategory)

        Subcategory_dropdown.select_by_visible_text(Attributes.Subcategory_value)

        points = Allocate_points_obj.Select_points()

        points.clear()

        points.send_keys(Attributes.Points_value)

        Allocate_points_obj.Select_message().send_keys(Attributes.Message_text)

        Allocate_points_obj.Enter_Remarks().send_keys(Attributes.Remarks_text)

        Allocate_points_obj.Submit_pointallocation()
        time.sleep(3)
