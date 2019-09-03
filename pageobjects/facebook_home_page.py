from generic.base import Base
from generic.loggingbase import logger as log

id_first_name="u_0_l"
id_last_name="u_0_n"
id_mobile_or_email="u_0_q"
id_password="u_0_x"
id_birth_day="day"
id_birth_month="month"
id_birth_year="year"
xpath_female_redio_button="//div[@id='u_0_10']/span/span/input[contains(text(),'Female')]"
xpath_male_redio_button="//span/label[contains(text(),'Male')]/preceding-sibling::input"
xpath_custom_redio_button="//div[@id='u_0_10']/span/span/input[@id='u_0_a']"
name_sign_up_button="websubmit"
css_first_name_error_msg="div.uiContextualLayerPositioner div#js_1zf"

class FaceBookHomePage(Base):

    def get_first_name_input_box_element(self):
        return self.identify_element("id",id_first_name)

    def enter_first_name_as(self,value):
        element=self.get_first_name_input_box_element()
        self.perform_actions(element,"settext",value=value)

    def get_last_name_input_box_element(self):
        return self.identify_element("id",id_last_name)

    def enter_last_name_as(self,value):
        element=self.get_last_name_input_box_element()
        self.perform_actions(element,"settext",value=value)

    def get_mobile_or_email_input_box_element(self):
        return self.identify_element("id",id_mobile_or_email)

    def enter_mobile_number_as(self,value):
        element=self.get_mobile_or_email_input_box_element()
        self.perform_actions(element,"settext",value=value)

    def get_password_input_box_element(self):
        return self.identify_element("id",id_password)

    def enter_password_as(self,value):
        element=self.get_password_input_box_element()
        self.perform_actions(element,"settext",value=value)

    def get_birth_day_dropdown_list_element(self):
        return self.identify_element("id",id_birth_day)

    def select_birth_day_as(self,value):
        element=self.get_birth_day_dropdown_list_element()
        self.perform_actions(element,"selectdropdown",others="index",value=value)

    def get_birth_month_dropdown_list_element(self):
        return self.identify_element("id",id_birth_month)

    def select_birth_month_as(self,value):
        element=self.get_birth_month_dropdown_list_element()
        self.perform_actions(element,"selectdropdown",others="value",value=value)


    def get_birth_year_dropdown_list_element(self):
        return self.identify_element("id",id_birth_year)

    def select_birth_year_as(self,value):
        element=self.get_birth_year_dropdown_list_element()
        self.perform_actions(element,"selectdropdown",others="visibletext",value=value)


    def get_gender_element_as_male(self):
        return self.identify_element("xpath",xpath_male_redio_button)

    def click_on_gender_as_male(self):
        element=self.get_gender_element_as_male()
        self.perform_actions(element,"click")

    def get_gender_element_as_female(self):
        return self.identify_element("xpath",xpath_female_redio_button)

    def click_on_gender_as_female(self):
        element=self.get_gender_element_as_female()
        self.perform_actions(element,"click")

    def get_gender_element_as_custom(self):
        return self.identify_element("xpath",xpath_custom_redio_button)

    def click_on_gender_as_custom(self):
        element=self.get_gender_element_as_custom()
        self.perform_actions(element,"click")

    def get_signup_button_element(self):
        return self.identify_element("name",name_sign_up_button)

    def click_on_sign_up_button(self):
        element=self.get_signup_button_element()
        self.perform_actions(element,"click")


    def get_first_name_error_msg_element(self):
        return self.identify_element("css",css_first_name_error_msg)

    def verify_first_name_error_msg(self):
        element=self.get_first_name_error_msg_element()
        self.perform_actions(element,"gettext")