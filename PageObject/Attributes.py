from selenium.webdriver.common.by import By



class Attributes:

                login_button = (By.XPATH, "//button[contains(text(),'Login')]")
                email_text_field = (By.XPATH, "//input[@placeholder='Email or username']")
                username_key = "nonhemanthwadiyar@gmail.com"
                password = (By.XPATH,"//input[@placeholder='Password']")
                password_key = 'pass'
                click_to_signin = (By.XPATH,"//button[normalize-space()='Sign In']")
                click_on_menu = (By.XPATH,"//img[@alt='User Image']")
                click_admin_fun = (By.XPATH,"//trn[normalize-space()='Admin Functions']")

                #Point Allocation
                point_allocation = (By.XPATH,"//trn[normalize-space()='Point allocation']")
                department_dropdown = (By.XPATH,"//select[@name='department']")
                department_value = "admin"

                user_dropdown = (By.XPATH,"//select[@ng-options='user as user.email for user in users']")
                User_selection = "test2@test.com"

                Point_categoru = (By.XPATH,"//select[@name='point_category']")
                Category_value  = "Appreciation"

                Point_SubCategory = (By.XPATH,"//select[@class='form-control ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
                Subcategory_value = "Good jon"

                Points = (By.XPATH,"//input[@name='points']")
                Points_value = '10'

                Message = (By.XPATH,"//textarea[@placeholder='This will be sent to user']")
                Message_text = "We can select a drop-down menu option value with Selenium webdriver. The Select class in Selenium is used to handle drop-down"
                Remarks = (By.XPATH,"//textarea[@placeholder='This will be saved for reference']")
                Remarks_text = "How to select a drop-down menu option value with Selenium (Python)? We can select a drop-down menu option value with Selenium webdriver." \
                               "The Select class in Selenium is used to handle drop-down. In an html document, the drop-down is identified with the "
                point_submit = (By.XPATH,"//trn[normalize-space()='Submit']")

                # Bulk point allocation

                bulk_point = (By.XPATH,"//trn[normalize-space()='or Allocate points in bulk']")
                Choose_files = (By.XPATH, "//input[@type='file']")
                send_email = (By.XPATH,"//div[@class='col-sm-4 col-sm-offset-2']//div[1]//label[1]//span[1]")
                send_push = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[2]/div[1]/div[1]/div[2]/label[1]/span[1]")
                submit = (By.XPATH,"//trn[contains(text(),'Submit')]")

                #Annoncement

                annoucement = (By.XPATH,"//trn[contains(text(),'Announcements')]")
                create_announcement = (By.XPATH,"//trn[contains(text(),'Create an announcement')]")
                annoucement_name = (By.XPATH,"//input[@ng-model='announcement.name']")
                annoucement_org = (By.XPATH,"//option[@value='number:47']")
                annoucement_dept = (By.XPATH,"//option[@value='number:362']")
                announcement_image = (By.XPATH,"//input[@id='fileInput']")
                annoucement_file = (By.XPATH,"//input[@class='form-control']")
                select_url = (By.XPATH,"//input[@placeholder='http://example.com']")
                click_start_date = (By.XPATH,"//a[@id='dropdown2']//div[@class='input-group']//span[@class='input-group-addon']//i[@class='glyphicon glyphicon-calendar']")
                select_start_date = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[10]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[4]/td[3]")
                select_time = (By.XPATH,"//span[normalize-space()='12:00 AM']")
                select_precise_time = (By.XPATH,"//span[normalize-space()='12:00 AM']")
                click_end_date = (By.XPATH,"//a[@id='dropdown3']//i[@class='glyphicon glyphicon-calendar']")
                select_end_date = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[11]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]")
                select_end_time = (By.XPATH,"//span[contains(text(),'12:00 AM')]")
                select_precise_end_time = (By.XPATH,"//span[contains(text(),'12:30 AM')]")
                is_priority= (By.XPATH,"//span[@class='fa fa-check']")
                click_ann_submit = (By.XPATH,"//trn[normalize-space()='Submit']")
                select_diff_month = (By.XPATH,"//div[@data-ng-model='announcement.end']//i[@class='glyphicon glyphicon-arrow-right']")
                enter_description = (By.ID,"tinymce")

                # Edit announcement
                edit_announcement = (By.XPATH,"//em[@class='fa fa-edit']")
                select_new_start_date = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[10]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
                select_new_end_date = (By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[11]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[5]/td[7]")
                select_new_start_month = (By.XPATH,"//div[@data-ng-model='announcement.start']//i[@class='glyphicon glyphicon-arrow-right']")
                new_announcement_name = (By.XPATH,"//input[@ng-model='announcement.name']")
                edit_submit = (By.XPATH,"//button[normalize-space()='Submit']")

                # Delete Announcemnet

                delete_announcement= (By.XPATH,"//em[@class='fa fa-trash-o']")
                confirm_delete_announcement = (By.XPATH,"//span[normalize-space()='Delete']")

                # Event creation

                event_tab = (By.XPATH,"//trn[@translate='events_capital']")
                click_create_event = (By.XPATH,"//trn[normalize-space()='Create an Event']")
                event_name = (By.XPATH,"//input[@ng-model='event.name']")
                event_department = (By.XPATH,"//option[@value='number:362']")
                select_contact = (By.XPATH,"//select[@name='contact_details']")
                event_type = (By.XPATH,"//select[@name='event_type']")
                event_max_capacity = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[8]/div[1]/div[1]/input[1]")
                event_image = (By.XPATH,"//input[@id='fileInput']")
                event_location = (By.XPATH,"//input[@placeholder='enter a location']")
                event_points = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[17]/div[1]/div[1]/input[1]")
                event_password = (By.XPATH,"//input[@ng-model='event.password']")
                click_event_start = (By.XPATH,"//a[@id='dropdown2']//i[@class='glyphicon glyphicon-calendar']")
                click_right_arrow = (By.XPATH,"//div[@data-ng-model='event.start']//th[@class='right']")
                select_event_start_date = (By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[20]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]")
                select_event_start_time = (By.XPATH,"//span[contains(text(),'12:00 AM')]")
                select_event_precise_time = (By.XPATH,"//span[contains(text(),'12:00 AM')]")
                click_event_end = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]/i[1]")
                click_end_right_arrow =(By.XPATH,"//div[@data-ng-model='event.end']//i[@class='glyphicon glyphicon-arrow-right']")
                select_event_end_date = (By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[5]/td[7]")
                select_event_end_time = (By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]")
                select_event_precise_end_time = (By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[21]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]")
                event_rsvp = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[22]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]/i[1]")
                rsvp_right = (By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[22]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/i[1]")
                rsvp_date = (By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/form[1]/fieldset[22]/div[1]/div[1]/div[1]/ul[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
                event_submit = (By.XPATH,"//button[normalize-space()='Submit']")

                #Edit event

                edit_event = (By.XPATH,"//em[@class='fa fa-edit']")
                new_event_name = (By.XPATH,"//input[@ng-model='event.name']")

                #delete Event

                delete_event = (By.XPATH,"//em[@class='fa fa-trash-o']")
                confirm_delete_event = (By.XPATH,"//span[normalize-space()='Delete']")

                #Edit point allocation

                transaction_history = (By.XPATH,"//trn[normalize-space()='Transactions History']")
                click_edit_points = (By.XPATH,"//tbody[1]/tr[1]/td[8]/a[1]")
                change_points = (By.XPATH,"//input[@name='points']")
                click_update = (By.XPATH,"//button[contains(text(),'Update')]")

                # Download report

                report_download = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[1]/div[1]/div[2]/select[1]")
                filter_by = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[1]/div[1]/div[3]/div[1]/select[1]")
                export_csv = (By.XPATH,"//trn[contains(text(),'Export as CSV')]")
                download_csv = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[1]/div[4]/div[5]/div[2]/div[1]/div[1]/div[2]/a[1]")

                # Push notification
                click_push_notification= (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/trn[1]")
                click_organization = (By.XPATH,"//option[contains(text(),'* DONT USE* Tester AUTO Org (Demo)')]")
                click_department = (By.XPATH,"//option[contains(text(),'admin')]")
                search_recipients = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[2]/div[2]/form[1]/fieldset[4]/div[1]/div[1]/tags-input[1]/div[1]/div[1]/input[1]")
                select_notification_type = (By.XPATH,"//body/div[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/div[2]/div[2]/form[1]/fieldset[5]/div[1]/div[1]/select[1]")
                enter_url = (By.XPATH,"//input[@id='survey_input']")
                select_image = (By.XPATH,"//input[@id='fileInput']")
                enter_message = (By.XPATH,"//textarea[@id='textArea']")
                click_send_notification = (By.XPATH,"//trn[normalize-space()='Send notification']")
                click_confirm_notification = (By.XPATH,"//span[contains(text(),'Send')]")







