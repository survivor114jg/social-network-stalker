import requests

from bs4 import BeautifulSoup
from services import config

class Twitter():

    TWITTER_BASE_URL = "https://twitter.com"

    config_service = config.Config()

    def get_twitter_data_from_account(self):
        twitter_full_url = self.get_twitter_full_url()
        http_response = requests.get(twitter_full_url)
        soup_response = BeautifulSoup(http_response.content, "html.parser")

        twitter_count = soup_response\
            .find("li", recursive=True, class_="ProfileNav-item--tweets")\
            .find("span", recursive=True, class_="ProfileNav-value")\
            .attrs['data-count']

        twitter_data = {
            "twitter_count": twitter_count
        }

        return twitter_data

    def get_twitter_full_url(self):
        twitter_full_url = self.TWITTER_BASE_URL + "/" + self.config_service.get_twitter_account()
        return twitter_full_url
