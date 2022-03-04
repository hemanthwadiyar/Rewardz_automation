from selenium.webdriver.common.by import By


class RewardzPage:

    def __init__(self, driver):
        self.driver = driver

    rewards = (By.XPATH, "//trn[normalize-space()='Rewards']")
    pointsrewards = (By.XPATH,"//trn[normalize-space()='Point Rewards']")
    evoucher = (By.XPATH,"//div[contains(text(),'e-Voucher')]")
    clickreward = (By.XPATH,"//strong[contains(text(),'Adidas $20 (Demo)')]")
    redeem = (By.XPATH,"//trn[normalize-space()='Redeem']")
    alert = (By.XPATH,"//span[@class='ng-binding ng-scope']")
    search = (By.XPATH,"//input[@placeholder='Search']")
    submit = (By.XPATH,"//trn[normalize-space()='Submit']")
    top_up = (By.XPATH,"//strong[@class='media-heading text-primary ng-binding']")
    clickredeemtop_up = (By.XPATH,"//button[contains(@type,'button')]")
    enterphone_number = (By.XPATH,"//input[@class='form-control input-md ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
    Mobile_redeem = (By.XPATH,"//button[@type='submit']//trn[@class='ng-scope'][contains(text(),'Redeem')]")
    filter = (By.XPATH,"//i[@class='fa fa-filter']")
    cancel = (By.XPATH,"//button[@ng-click='cancel()']")
    physical = (By.XPATH,"//div[contains(text(),'Physical Voucher')]")
    demophysicalvoucher = (By.XPATH,"//a[@class='ng-binding']")
    Physicalvoucher = (By.XPATH,"//strong[@class='media-heading text-primary ng-binding']")
    increment = (By.XPATH,"//button[normalize-space()='+']")
    physicalredeem = (By.XPATH,"//trn[normalize-space()='Redeem']")
    ecash = (By.XPATH,"//strong[@class='media-heading text-primary ng-binding']")
    eredeem = (By.XPATH,"//trn[normalize-space()='Redeem']")
    amount = (By.XPATH,"//input[@placeholder='1']")
    ePhoneNumber = (By.XPATH,"//input[@type='text']")
    epredeem = (By.XPATH,"//button[@type='submit']//trn[@class='ng-scope'][normalize-space()='Redeem']")
    qr_list = (By.XPATH,"//div[@class='media-body clearfix']")
    qr_redeem = (By.XPATH,"//trn[normalize-space()='Redeem']")
    barcode_list = (By.XPATH,"//strong[contains(text(),'Barcode Agoda HKD 100 (Demo)')]")
    barcode_redeem = (By.XPATH,"//trn[normalize-space()='Redeem']")
    physical_delivery = (By.XPATH,"//strong[@class='media-heading text-primary ng-binding']")
    increment_physical = (By.XPATH,"//button[normalize-space()='+']")
    redeem_physical = (By.XPATH,"//trn[normalize-space()='Redeem']")

    click_menu = (By.XPATH,"//trn[normalize-space()='Rewards']")
    click_discount_reward = (By.XPATH,"//trn[normalize-space()='Discount Rewards']")
    select_discount_reward = (By.XPATH,"//strong[@class='media-heading text-primary ng-binding']")

    def clickRewards(self):
        return self.driver.find_element(*RewardzPage.rewards)

    def clickPoints(self):
        return self.driver.find_element(*RewardzPage.pointsrewards)

    def clickEvoucher(self):
        return self.driver.find_element(*RewardzPage.evoucher)

    def clickonIndomart(self):
        return self.driver.find_element(*RewardzPage.clickreward)

    def RedeemReward(self):
        return self.driver.find_element(*RewardzPage.redeem)

    def AlertMessage(self):
        return self.driver.find_element(*RewardzPage.alert)

    def Search(self):
        return self.driver.find_element(*RewardzPage.search)

    def Submit(self):
        return self.driver.find_element(*RewardzPage.submit)

    def RedeemTop_up(self):
        return self.driver.find_element(*RewardzPage.top_up)

    def ClickRedeemTop_up(self):
        return self.driver.find_element(*RewardzPage.clickredeemtop_up)

    def EnterPhoneNumber(self):
        return self.driver.find_element(*RewardzPage.enterphone_number)

    def ClickRedeemTop_upButton(self):
        return self.driver.find_element(*RewardzPage.Mobile_redeem)

    def ClickFilter(self):
        return self.driver.find_element(*RewardzPage.filter)

    def ClickCancel(self):
        return self.driver.find_element(*RewardzPage.cancel)

    def ClickPhysical(self):
        return self.driver.find_element(*RewardzPage.physical)

    def clickDemoFilter(self):
        return self.driver.find_element(*RewardzPage.demophysicalvoucher)

    def clickPhysicalVoucher(self):
        return self.driver.find_element(*RewardzPage.Physicalvoucher)

    def clickPlus(self):
        return self.driver.find_element(*RewardzPage.increment)

    def clickRedeemPhysical(self):
        return self.driver.find_element(*RewardzPage.physicalredeem)

    def clickEcash(self):
        return self.driver.find_element(*RewardzPage.ecash)

    def clickeRedeem(self):
        return self.driver.find_element(*RewardzPage.eredeem)

    def enterAmount(self):
        return self.driver.find_element(*RewardzPage.amount)

    def enterEPhoneNumber(self):
        return self.driver.find_element(*RewardzPage.ePhoneNumber)

    def clickEPRedeem(self):
        return self.driver.find_element(*RewardzPage.epredeem)

    def qrReward(self):
        return self.driver.find_element(*RewardzPage.qr_list)

    def qrRedeem(self):
        return self.driver.find_element(*RewardzPage.qr_redeem)

    def BarcodeReward(self):
        return self.driver.find_element(*RewardzPage.barcode_list)

    def BarcodeRedeem(self):
        return self.driver.find_element(*RewardzPage.barcode_redeem)

    def Physical_Delivery(self):
        return self.driver.find_element(*RewardzPage.physical_delivery)

    def Increment_Physical(self):
        return self.driver.find_element(*RewardzPage.increment_physical)

    def Redeem_Physical(self):
        return self.driver.find_element(*RewardzPage.redeem_physical)

    def Click_Menu(self):
        return self.driver.find_element(*RewardzPage.click_menu)

    def Click_Discount_Reward(self):
        return self.driver.find_element(*RewardzPage.click_discount_reward)

    def Select_Discount_Reward(self):
        return self.driver.find_element(*RewardzPage.select_discount_reward)


