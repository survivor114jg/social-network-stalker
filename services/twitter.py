from bs4 import BeautifulSoup
from services import config

class Twitter():

    config_service = config.Config()

    def get_twitter_data_from_account(self):

        self.config_service.getTwitterAccount()

        return