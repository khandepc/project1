from generic.base import Base
from generic.loggingbase import logger as log
name_google_search_box="q"
xpath_google_search="//div[2]/center/input[1]"
partial_link_chetan="Chetan Gautam Bendre"


class AllLinksText(Base):

    def get_google_search_input_box(self):
        return self.identify_element("name",name_google_search_box)

    def enter_value_to_search_in_google_search(self,value):
        log.info("enter value to search as",value)
        element=self.get_google_search_input_box()
        self.perform_actions(element,"settext",value)

    def get_google_search_button(self):
        return self.identify_element("xpath",xpath_google_search)

    def click_on_google_search_button(self):
        log.info("click on google search")
        element=self.get_google_search_button()
        self.perform_actions(element,"click")

    def get_all_links_chetan(self):
        return self.identify_elements("partiallinktext",partial_link_chetan)

    def collect_all_links_text_of_chetan(self):
        log.info("collect all texts")
        elements=self.get_all_links_chetan()
        all_result_text=[]
        log.info(all_result_text)
        for link in elements:
            all_result_text.append(self.perform_actions(link,"gettext"))
