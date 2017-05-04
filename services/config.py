import ConfigParser

class Config:

    social_network_section = "SocialNetwork"
    twitter_account_config_key = "twitter_account"
    config_parser = None

    def __init__(self):

        self.config_parser = ConfigParser.ConfigParser()
        self.config_parser.readfp(open("config.cfg"))

    def get_twitter_account(self):

        twitter_account = self.config_parser.get(self.social_network_section, self.twitter_account_config_key)

        return twitter_account