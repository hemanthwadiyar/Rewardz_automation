import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.RewardsPage import RewardzPage
from PageObject.SignInPage import Signin_page
from Utilities.BaseClass import BaseClass

Chrome_options = webdriver.ChromeOptions

class TestOne(BaseClass):

    def test_e2e(self, setup):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5)
        log = self.getLogger()
        # Signin Page elements
        Signin_obj = Signin_page(self.driver)
        Signin_obj.signin_path().click()
        log.info("clicked on sign in")
        Signin_obj.Email_path().send_keys(Signin_page.username_key)
        Signin_obj.Password_path()
        Signin_obj.Sigin_path().click()
        get_title = self.driver.title
        log.info(get_title)
        time.sleep(2)

        rewardspage = RewardzPage(self.driver)

        log.info("Clicking on rewards")
        time.sleep(2)
        rewardspage.clickRewards().click()
        log.info("Clicking on point rewards")
        time.sleep(2)
        rewardspage.clickPoints().click()
        log.info("Clicked on point reward")
        log.info("Clicking on E-voucher")
        time.sleep(2)
        rewardspage.clickEvoucher().click()
        time.sleep(1)
        log.info("Clicking on IndoMart voucher ")
        time.sleep(2)
        rewardspage.clickonIndomart().click()
        log.info("Redeeming the reward")
        time.sleep(5)
        rewardspage.RedeemReward().click()
        log.info("clicked on redeem")
        time.sleep(2)
        alert = self.driver.switch_to.alert
        log.info("Switched to alert")
        alert.accept()
        log.info("accepted the alert")
        #alt_msg = rewardspage.AlertMessage().text
        time.sleep(2)
        #print(alt_msg)
        log.info("")
        #assert "successfully redeemed" in alt_msg
        self.driver.get_screenshot_as_file("e-1voucher.png")
        print("-------E-Voucher redemption successful")
        log.info("-------E-Voucher redemption successful")
        time.sleep(5)
        #self.driver.back()
        time.sleep(5)
        log.info("Redeemed e-voucher")

        '''
        #Mobile pulsa redemtion

        self.driver.back()
        print("Current Page title after back: ", self.driver.title)
        time.sleep(2)
        rewardspage.Search().send_keys("Mobile")
        log.info("Clicking on mobile pulsa")
        time.sleep(2)
        rewardspage.Submit().click()
        time.sleep(2)
        rewardspage.RedeemTop_up().click()
        log.info("redeeming mobile pulsa")
        time.sleep(2)
        rewardspage.ClickRedeemTop_up().click()
        time.sleep(2)
        rewardspage.EnterPhoneNumber().send_keys("8867755618")
        time.sleep(2)
        rewardspage.ClickRedeemTop_upButton().click()
        try:
            alert1 = self.driver.switch_to.alert
            alert1.accept()
            print("alert accepted")
        except:
            print("Alert message not accepted")
        rewardspage.ClickCancel().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("top-up.png")

        #Redeem Physical vouchers
        
        self.driver.back()
        print("Current Page title after back: ", self.driver.title)
        time.sleep(2)
        log.info("Clicking on physical rewards")
        rewardspage.ClickPhysical().click()
        log.info("Clicking on filter")
        time.sleep(2)
        rewardspage.ClickFilter().click()
        time.sleep(2)
        rewardspage.clickDemoFilter().click()
        time.sleep(2)
        log.info("Clicking on Physical voucher")
        rewardspage.clickPhysicalVoucher().click()
        time.sleep(2)
        #rewardspage.clickPlus().click()
        rewardspage.clickRedeemPhysical().click()
        try:
            alert2 = self.driver.switch_to.alert
            alert2.accept()
            print("alert accepted")
            log.info("alert accepted")
        except:
            print("Alert message not accepted")
        time.sleep(2)
        self.driver.get_screenshot_as_file("physical.png")

        # Redeeming Barcode Voucher
        self.driver.back()
        print("Current Page title after back: ", self.driver.title)
        time.sleep(1)
        rewardspage.Search().send_keys("Barcode")
        rewardspage.Submit().click()
        time.sleep(2)
        log.info("BarCode voucher")
        rewardspage.BarcodeReward().click()
        time.sleep(2)
        rewardspage.BarcodeRedeem().click()
        try:
            alert3 = self.driver.switch_to.alert
            alert3.accept()
            print("alert accepted")
            log.info("Alert accepted")
        except:
            print("Alert message not accepted")

        # redeeming QR Voucher
        self.driver.back()
        print("Current Page title after back: ", self.driver.title)
        time.sleep(2)
        rewardspage.Search().send_keys("qr code")
        time.sleep(2)
        rewardspage.Submit().click()
        time.sleep(2)
        log.info("QR voucher")
        rewardspage.qrReward().click()
        rewardspage.qrRedeem().click()
        try:
            alert3 = self.driver.switch_to.alert
            alert3.accept()
            print("alert accepted")
            log.info("Alert accepted")
        except:
            print("Alert message not accepted")
        '''
        #Redeeming Physical Delivery

        self.driver.back()
        print("Current Page title after back: ", self.driver.title)
        time.sleep(2)
        rewardspage.Search().send_keys("Physical Delivery")
        time.sleep(2)
        rewardspage.Submit().click()
        time.sleep(2)
        log.info("Searched for Physical Delivery ")
        rewardspage.Physical_Delivery().click()
        time.sleep(2)
        log.info("Clicked on physical Delivery")
        rewardspage.Increment_Physical().click()
        time.sleep(2)
        log.info(("Incremented  physical quantity "))
        rewardspage.Redeem_Physical().click()
        log.info("Redeemed Physical voucher")
        try:
            alert3 = self.driver.switch_to.alert
            alert3.accept()
            print("alert accepted")
            log.info("Alert accepted")
        except:
            print("Alert message not accepted")

        time.sleep(3)

        # click on discount rewards

        rewardspage.Click_Menu().click()
        log.info("Clicked on rewards")
        time.sleep(3)
        print("Current Page title after back: ", self.driver.title)
        rewardspage.Click_Discount_Reward().click()
        log.info("Clicked on Discount rewards")
        time.sleep(2)
        rewardspage.Select_Discount_Reward().click()
        log.info("Selected the discount reward")
        time.sleep(2)
        self.driver.get_screenshot_as_file("Discount.png")








