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

        tweets_count = soup_response\
            .find("li", recursive=True, class_="ProfileNav-item--tweets")\
            .find("span", recursive=True, class_="ProfileNav-value")\
            .attrs['data-count']

        following_count = soup_response\
            .find("li", recursive=True, class_="ProfileNav-item--following")\
            .find("span", recursive=True, class_="ProfileNav-value")\
            .attrs['data-count']

        followers_count = soup_response\
            .find("li", recursive=True, class_="ProfileNav-item--followers")\
            .find("span", recursive=True, class_="ProfileNav-value")\
            .attrs['data-count']

        likes_count = soup_response\
            .find("li", recursive=True, class_="ProfileNav-item--favorites")\
            .find("span", recursive=True, class_="ProfileNav-value")\
            .attrs['data-count']

        twitter_data = {
            "tweets_count": tweets_count,
            "following_count": following_count,
            "followers_count": followers_count,
            "likes_count": likes_count
        }

        return twitter_data

    def get_twitter_full_url(self):
        twitter_full_url = self.TWITTER_BASE_URL + "/" + self.config_service.get_twitter_account()
        return twitter_full_url
