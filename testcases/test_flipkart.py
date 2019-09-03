from pageobjects.flipkart_page import TestFlipkart
import pytest

class TestFlipkartMi(TestFlipkart):

    @pytest.fixture()
    def launch_app(self):
        dd=self.read_config_file("base.ini","common3")
        self.launch_application(dd["browser"],dd["url"])
        yield
        self.close_application()

    def test_flipkart_mi_click(self,launch_app):
        self.click_on_close_popup()
        self.move_on_electronics()
        self.click_on_mi()