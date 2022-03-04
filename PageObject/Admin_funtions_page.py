from PageObject.Attributes import Attributes


class Admin_Page(Attributes):

    def __init__(self,driver):
        self.driver = driver

    def allocate_point(self):
        return self.driver.find_element(*Attributes.point_allocation)

    def Select_department(self):
        return self.driver.find_element(*Attributes.department_dropdown)

    def Select_user(self):
        return self.driver.find_element(*Attributes.user_dropdown)

    def Select_category(self):
        return self.driver.find_element(*Attributes.Point_categoru)

    def Select_SubCategory(self):
        return self.driver.find_element(*Attributes.Point_SubCategory)

    def Select_points(self):
        return self.driver.find_element(*Attributes.Points)

    def Select_message(self):
        return self.driver.find_element(*Attributes.Message)

    def Enter_Remarks(self):
        return self.driver.find_element(*Attributes.Remarks)

    def Submit_pointallocation(self):
        return self.driver.find_element(*Attributes.point_submit).click()

    def Bulk_pointallocation(self):
        return self.driver.find_element(*Attributes.bulk_point)

    def Choose_file(self):
        return self.driver.find_element(*Attributes.Choose_files)

    def Send_email(self):
        return self.driver.find_element(*Attributes.send_email)

    def Send_push(self):
        return self.driver.find_element(*Attributes.send_push)

    def Submit(self):
        return self.driver.find_element(*Attributes.submit)

    def Announcement(self):
        return self.driver.find_element(*Attributes.annoucement)

    def Create_Announcement(self):
        return self.driver.find_element(*Attributes.create_announcement)

    def Announcement_name(self):
        return self.driver.find_element(*Attributes.annoucement_name)

    def Select_ann_organization(self):
        return self.driver.find_element(*Attributes.annoucement_org)

    def Select_ann_department(self):
        return self.driver.find_element(*Attributes.annoucement_dept)

    def Select_image(self):
        return self.driver.find_element(*Attributes.announcement_image)

    def Select_file(self):
        return self.driver.find_element(*Attributes.annoucement_file)

    def Give_URL(self):
        return self.driver.find_element(*Attributes.select_url)

    def Click_start_date(self):
        return self.driver.find_element(*Attributes.click_start_date)

    def Select_start_date(self):
        return self.driver.find_element(*Attributes.select_start_date)

    def Select_Precise_time(self):
        return self.driver.find_element(*Attributes.select_precise_time)

    def Select_time(self):
        return self.driver.find_element(*Attributes.select_time)

    def Click_end_date(self):
        return self.driver.find_element(*Attributes.click_end_date)

    def Select_end_date(self):
        return self.driver.find_element(*Attributes.select_end_date)

    def Select_end_time(self):
        return self.driver.find_element(*Attributes.select_end_time)

    def Select_precise_end_time(self):
        return self.driver.find_element(*Attributes.select_precise_end_time)

    def Select_is_priority(self):
        return self.driver.find_element(*Attributes.is_priority)

    def Click_Ann_submit(self):
        return self.driver.find_element(*Attributes.click_ann_submit).click()

    def Select_diff_month(self):
        return self.driver.find_element(*Attributes.select_diff_month)

    def Enter_description(self):
        return self.driver.find_element(*Attributes.enter_description)

    def Edit_Announcement(self):
        return self.driver.find_element(*Attributes.edit_announcement)

    def New_start_date(self):
        return self.driver.find_element(*Attributes.select_new_start_date)

    def New_end_date(self):
        return self.driver.find_element(*Attributes.select_new_end_date)

    def Select_new_start_month(self):
        return self.driver.find_element(*Attributes.select_new_start_month)

    def New_announcement_name(self):
        return self.driver.find_element(*Attributes.new_announcement_name)

    def Edit_submit(self):
        return self.driver.find_element(*Attributes.edit_submit)

    def Event_tab(self):
        return self.driver.find_element(*Attributes.event_tab)

    def Click_Create_evemt(self):
        return self.driver.find_element(*Attributes.click_create_event)

    def Event_Name(self):
        return self.driver.find_element(*Attributes.event_name)

    def Event_Department(self):
        return self.driver.find_element(*Attributes.event_department)

    def Select_contact(self):
        return self.driver.find_element(*Attributes.select_contact)

    def Event_type(self):
        return self.driver.find_element(*Attributes.event_type)

    def Event_Max_Capacity(self):
        return self.driver.find_element(*Attributes.event_max_capacity)

    def Event_Image(self):
        return self.driver.find_element(*Attributes.event_image)

    def Event_Location(self):
        return self.driver.find_element(*Attributes.event_location)

    def Event_points(self):
        return self.driver.find_element(*Attributes.event_points)

    def Event_Password(self):
        return self.driver.find_element(*Attributes.event_password)

    def Click_Event_start(self):
        return self.driver.find_element(*Attributes.click_event_start)

    def Click_right_arrow(self):
        return self.driver.find_element(*Attributes.click_right_arrow)

    def Select_event_start_date(self):
        return self.driver.find_element(*Attributes.select_event_start_date)

    def Select_event_start_time(self):
        return self.driver.find_element(*Attributes.select_event_start_time)

    def Select_event_precise_time(self):
        return self.driver.find_element(*Attributes.select_event_precise_time)

    def Click_Event_end(self):
        return self.driver.find_element(*Attributes.click_event_end)

    def Click_end_right_arrow(self):
        return self.driver.find_element(*Attributes.click_end_right_arrow)

    def Select_event_end_date(self):
        return self.driver.find_element(*Attributes.select_event_end_date)

    def Select_event_end_time(self):
        return self.driver.find_element(*Attributes.select_event_end_time)

    def Select_event_precise_end_time(self):
        return self.driver.find_element(*Attributes.select_event_precise_end_time)

    def Event_RSVP(self):
        return self.driver.find_element(*Attributes.event_rsvp)

    def RSVP_right(self):
        return self.driver.find_element(*Attributes.rsvp_right)

    def RSVP_date(self):
        return self.driver.find_element(*Attributes.rsvp_date)

    def Event_submit(self):
        return self.driver.find_element(*Attributes.event_submit)

    def Delete_Announcement(self):
        return self.driver.find_element(*Attributes.delete_announcement)

    def Confirm_Delete_Announcement(self):
        return self.driver.find_element(*Attributes.confirm_delete_announcement)

    def Edit_Event(self):
        return self.driver.find_element(*Attributes.edit_event)

    def New_Event_Name(self):
        return self.driver.find_element(*Attributes.new_event_name)

    def Delete_Event(self):
        return self.driver.find_element(*Attributes.delete_event)

    def Confirm_Delete_Event(self):
        return self.driver.find_element(*Attributes.confirm_delete_event)

    def Transaction_History(self):
        return self.driver.find_element(*Attributes.transaction_history)

    def Click_Edit_points(self):
        return self.driver.find_element(*Attributes.click_edit_points)

    def Change_points(self):
        return self.driver.find_element(*Attributes.change_points)

    def Click_Update(self):
        return self.driver.find_element(*Attributes.click_update)

    def Report_Download(self):
        return self.driver.find_element(*Attributes.report_download)

    def Filter_by(self):
        return self.driver.find_element(*Attributes.filter_by)

    def Export_CSV(self):
        return self.driver.find_element(*Attributes.export_csv)

    def Download_CSV(self):
        return self.driver.find_element(*Attributes.download_csv)

    def Click_push_notification(self):
        return self.driver.find_element(*Attributes.click_push_notification)

    def Click_organization(self):
        return self.driver.find_element(*Attributes.click_organization)

    def Click_Department(self):
        return self.driver.find_element(*Attributes.click_department)

    def Search_recipient(self):
        return self.driver.find_element(*Attributes.search_recipients)

    def Select_Notification_type(self):
        return self.driver.find_element(*Attributes.select_notification_type)

    def Enter_url(self):
        return self.driver.find_element(*Attributes.enter_url)

    def Select_notification_image(self):
        return self.driver.find_element(*Attributes.select_image)

    def Enter_message(self):
        return self.driver.find_element(*Attributes.enter_message)

    def Click_send_notification(self):
        return self.driver.find_element(*Attributes.click_send_notification)

    def Click_confirm_notification(self):
        return self.driver.find_element(*Attributes.click_confirm_notification)















