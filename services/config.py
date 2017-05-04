import ConfigParser

class Config:

    SOCIAL_NETWORK_SECTION = "SocialNetwork"
    TWITTER_ACCOUNT_CONFIG_KEY = "twitter_account"

    config_parser = None

    def __init__(self):
        self.config_parser = ConfigParser.ConfigParser()
        self.config_parser.readfp(open("config.cfg"))

    def get_twitter_account(self):
        twitter_account = self.config_parser.get(self.SOCIAL_NETWORK_SECTION, self.TWITTER_ACCOUNT_CONFIG_KEY)
        return twitter_account