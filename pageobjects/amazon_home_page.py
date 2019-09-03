from generic.base import Base

xpath_category="//div[@id='nav-main']/div/div[@id='nav-shop']/a/span[2]"
xpath_mobile_and_computers="//div/span[6]"
xpath_all_mobile_phones="//div/div/a/span[contains(text(),'All Mobile Phones')]"


class AmazonHome(Base):

    def get_category_element(self):
        return self.identify_element("xpath",xpath_category)


    def get_mobile_and_computer_element(self):
        return self.identify_element("xpath",xpath_mobile_and_computers)


    def get_all_mobile_phones_element(self):
        return self.identify_element("xpath",xpath_all_mobile_phones)


    def move_to_category(self):
        return self.perform_mouse_keyboard_actions("movetoelement",self.get_category_element())

    def move_to_mobile_and_computers(self):
        return self.perform_mouse_keyboard_actions("movetoelement",self.get_mobile_and_computer_element())

    def move_to_all_mobile_phones(self):
        return self.perform_mouse_keyboard_actions("movetoelement",self.get_all_mobile_phones_element())

    def click_on_all_mobile_phones(self):
        self.perform_mouse_keyboard_actions("click",self.move_to_all_mobile_phones())
