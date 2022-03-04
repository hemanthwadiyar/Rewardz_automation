import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","/Users/mac/Downloads")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(executable_path="/Users/mac/Desktop/RewardzProject/Driver/geckodriver",firefox_profile=fp)

driver.get("https://cerrapoints.com/Dashboard")
time.sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-default login-top']").click()
time.sleep(1)
username = driver.find_element_by_xpath("//body[@class='modal-open']/div[@id='main_container']/div[@id='LoginModal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='form-sec']/div[contains(@class,'row')]/div[@class='col-sm-8 ng-scope']/form[@id='login-form']/input[1]")
username.send_keys("nonhemanthwadiyar@gmail.com")
driver.maximize_window()

driver.find_element_by_xpath("//input[@type='password']").send_keys("pass")
driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()
time.sleep(5)
driver.find_element_by_xpath("//img[@class='user-image']").click()
time.sleep(2)
driver.find_element_by_xpath("//trn[contains(text(),'Admin Functions')]").click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 4000)")
time.sleep(2)

x = driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[1]/div[1]/div[2]/select[1]")
time.sleep(2)
drop = Select(x)
drop.select_by_visible_text("Users")
time.sleep(2)


y = driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[1]/div[1]/div[3]/div[1]/select[1]")

drop2 = Select(y)
drop2.select_by_visible_text("Overall")
time.sleep(2)

driver.find_element_by_xpath("//trn[contains(text(),'Export as CSV')]").click()

time.sleep(5)

driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[2]/div[1]/div[1]/div[2]/a[1]").click()




'''
driver.find_element_by_xpath("//trn[contains(text(),'Announcements')]").click()
time.sleep(1)
driver.find_element_by_xpath("//trn[contains(text(),'Create an announcement')]").click()
#driver.execute_script("window.scrollTo({},{});".format(0,1000))

time.sleep(5)

name = driver.find_element_by_xpath("//input[@ng-model='announcement.name']").send_keys("testing announcement 1")

#driver.find_element_by_xpath("//option[@value='number:47']").click()
driver.find_element_by_xpath("//option[@value='number:362']").click()
time.sleep(1)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='ui-tinymce-2_ifr']"))
driver.find_element_by_xpath("//body[@id='tinymce']").click()
driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("Description")
driver.switch_to.default_content()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='fileInput']").send_keys("/Users/mac/Desktop/2021-05-30 01.12.12.jpg")
driver.find_element_by_xpath("//input[@class='form-control']").send_keys("/Users/mac/Desktop/2021-05-30 01.12.12.jpg")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='http://example.com']").send_keys("https://canvas.instructure.com/courses/2412303")
time.sleep(1)
driver.find_element_by_xpath("//a[@id='dropdown2']//div[@class='input-group']//span[@class='input-group-addon']//i[@class='glyphicon glyphicon-calendar']").click()
time.sleep(1)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[10]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[3]/td[5]").click()
time.sleep(1)
driver.find_element_by_xpath("//span[normalize-space()='12:00 AM']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[normalize-space()='12:00 AM']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@id='dropdown3']//i[@class='glyphicon glyphicon-calendar']").click()
time.sleep(1)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[11]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[4]/td[3]").click()
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'12:00 AM')]").click()
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'12:30 AM')]").click()
driver.find_element_by_xpath("//span[@class='fa fa-check']").click()
driver.find_element_by_xpath("//trn[normalize-space()='Submit']").click()
time.sleep(2)
'''








