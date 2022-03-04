import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="/Users/mac/Desktop/RewardzProject/Driver/geckodriver")

driver.get("https://cerrapoints.com/Dashboard")
time.sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-default login-top']").click()
time.sleep(1)
username = driver.find_element_by_xpath("//body[@class='modal-open']/div[@id='main_container']/div[@id='LoginModal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/div[@class='form-sec']/div[contains(@class,'row')]/div[@class='col-sm-8 ng-scope']/form[@id='login-form']/input[1]")
username.send_keys("hemanthwadiyar@gmail.com")
driver.maximize_window()

driver.find_element_by_xpath("//input[@type='password']").send_keys("pass")
driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()
time.sleep(5)
driver.find_element_by_xpath("//img[@class='user-image']").click()
time.sleep(2)
driver.find_element_by_xpath("//trn[contains(text(),'Admin Functions')]").click()
time.sleep(2)
############################################********************############################################
driver.find_element_by_xpath(("//trn[@translate='events_capital']")).click()
time.sleep(2)
driver.find_element_by_xpath(("//trn[normalize-space()='Create an Event']")).click()
time.sleep(2)
driver.find_element_by_xpath(("//input[@ng-model='event.name']")).send_keys("testing event")
driver.find_element_by_xpath("//option[@value='number:362']").click()
contact_detail = driver.find_element_by_xpath(("//select[@name='contact_details']"))
contact_detail.click()
drop = Select(contact_detail)
drop.select_by_visible_text("tester@org.com")

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='ui-tinymce-3_ifr']"))
driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("Event Description")
driver.switch_to.default_content()
time.sleep(1)
event_type = driver.find_element_by_xpath("//select[@name='event_type']")
event_type.click()
time.sleep(2)
drop_event_type = Select(event_type)
time.sleep(1)
drop_event_type.select_by_visible_text("Development")
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[8]/div[1]/div[1]/input[1]").clear()
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[8]/div[1]/div[1]/input[1]").send_keys("10")
driver.find_element_by_xpath("//input[@id='fileInput']").send_keys("/Users/mac/Downloads/1 Injasati SS/147,216.jpeg")
driver.find_element_by_xpath("//input[@placeholder='enter a location']").send_keys("Bengaluru, Karnataka, India")
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='enter a location']").send_keys(Keys.ARROW_DOWN)
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='enter a location']").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[17]/div[1]/div[1]/input[1]").click()
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[17]/div[1]/div[1]/input[1]").clear()
time.sleep(1)
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[17]/div[1]/div[1]/input[1]").send_keys("10")
driver.find_element_by_xpath("//input[@ng-model='event.password']").send_keys("pass")
driver.find_element_by_xpath("//a[@id='dropdown2']//i[@class='glyphicon glyphicon-calendar']").click()
driver.find_element_by_xpath("//div[@data-ng-model='event.start']//th[@class='right']").click()
driver.find_element_by_xpath("//div[@data-ng-model='event.start']//th[@class='right']").click()
driver.find_element_by_xpath("//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[20]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]").click()
driver.find_element_by_xpath("//span[contains(text(),'12:00 AM')]").click()
driver.find_element_by_xpath("//span[contains(text(),'12:00 AM')]").click()
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]/i[1]").click()
driver.find_element_by_xpath("//div[@class='datetimepicker table-responsive ng-isolate-scope ng-empty ng-valid ng-pristine']//table[@class='table table-condensed day-view']//th[@class='right']").click()
driver.find_element_by_xpath("//div[@class='datetimepicker table-responsive ng-isolate-scope ng-empty ng-valid ng-pristine']//table[@class='table table-condensed day-view']//th[@class='right']").click()
driver.find_element_by_xpath("//div[@class='datetimepicker table-responsive ng-isolate-scope ng-empty ng-valid ng-pristine']//table[@class='table table-condensed day-view']//th[@class='right']").click()
driver.find_element_by_xpath("//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[5]/td[7]").click()
driver.find_element_by_xpath("//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]").click()
driver.find_element_by_xpath("//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]").click()
driver.find_element_by_xpath("//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[22]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]/i[1]").click()
driver.execute_script("window.scrollTo({},{});".format(0,1000))
#mySelectElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[normalize-space()='17']")))
#mySelectElement.click()
driver.find_element_by_xpath("//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[22]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/i[1]").click()
driver.find_element_by_xpath("//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[22]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]").click()
time.sleep(1 )
driver.find_element_by_xpath("//trn[contains(text(),'Submit')]").click()

time.sleep(5)



