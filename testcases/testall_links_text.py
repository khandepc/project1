from pageobjects.all_links_text_page import AllLinksText

class TestAllLinksText(AllLinksText):

    def test_all_texts_of_links(self):
        # import pdb
        # pdb.set_trace()
        dd=self.read_config_file("base.ini","common2")
        self.launch_application(dd["browser"],dd["url"])
        self.enter_value_to_search_in_google_search("chetan gautam bendre")
        self.click_on_google_search_button()
        self.collect_all_links_text_of_chetan()
        self.close_application()
