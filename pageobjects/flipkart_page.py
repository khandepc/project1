from generic.base import Base



xpath_close_popup="//div[@class='mCRfo9']/div/div/button"
xpath_electronics="//div[@id='container']/div/div[2]/div/ul/li/span[contains(text(),'Electronics')]"
xpath_mi="//*[@id='container']/div/div[2]/div/ul/li[1]/ul/li/ul/li[1]/ul/li[2]/a"

class TestFlipkart(Base):

    def get_close_popup_element(self):
        return self.identify_element("xpath",xpath_close_popup)

    def click_on_close_popup(self):
        element=self.get_close_popup_element()
        self.perform_actions(element,"click")

    def get_electronics_element(self):
        return self.identify_element("xpath",xpath_electronics)

    def get_mi_element(self):
        return self.identify_element("xpath",xpath_mi)

    def move_on_electronics(self):
        return self.perform_mouse_keyboard_actions("movetoelement",self.get_electronics_element())

    def move_on_mi(self):
        return self.perform_mouse_keyboard_actions("movetoelement",self.get_mi_element())

    def click_on_mi(self):
        self.perform_mouse_keyboard_actions("click",self.move_on_mi())

