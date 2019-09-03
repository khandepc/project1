from pageobjects.facebook_home_page import FaceBookHomePage
from generic.loggingbase import logger as log
import pytest

class Test_facebook_home(FaceBookHomePage):

    @pytest.fixture()
    def launch_and_app(self):
        dd=self.read_config_file("base.ini","common")
        self.launch_application(dd["browser"],dd["url"])
        yield
        self.close_application()

    def test_functionality_of_facebook_home_page_with_valid_details(self,launch_and_app):
        self.enter_first_name_as("prashant")
        self.enter_last_name_as("khande")
        self.enter_mobile_number_as("8421835356")
        self.enter_password_as("khande123")
        self.select_birth_day_as(14)
        self.select_birth_month_as("9")
        self.select_birth_year_as("1996")
        self.click_on_gender_as_male()
        self.click_on_sign_up_button()

    def test_functionality_of_facebook_home_page_with_invalid_name(self,launch_and_app):
        self.enter_first_name_as("pr as ha nt 2 1 7 1")
        self.enter_last_name_as("khande")
        self.enter_mobile_number_as("8421835356")
        self.enter_password_as("khande123")
        self.select_birth_day_as(14)
        self.select_birth_month_as("9")
        self.select_birth_year_as("1996")
        self.click_on_gender_as_male()
        self.click_on_sign_up_button()

    def test_functionality_of_facebook_home_page_without_first_name(self,launch_and_app):
        self.enter_last_name_as("khande")
        self.enter_mobile_number_as("8421835356")
        self.enter_password_as("khande123")
        self.select_birth_day_as(14)
        self.select_birth_month_as("9")
        self.select_birth_year_as("1996")
        self.click_on_gender_as_male()
        self.click_on_sign_up_button()
        assert self.verify_first_name_error_msg()=="What's your name?"

