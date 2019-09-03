from pageobjects.amazon_home_page import AmazonHome
import pytest


class TestAmazonAllMobiles(AmazonHome):


    @pytest.fixture()
    def launch_app(self):
        dd=self.read_config_file("base.ini","common4")
        self.launch_application(dd["browser"],dd["url"])
        yield
        self.close_application()

    def test_click_on_all_mobile_phones(self,launch_app):
        self.move_to_category()
        self.move_to_mobile_and_computers()
        self.move_to_all_mobile_phones()
        self.click_on_all_mobile_phones()