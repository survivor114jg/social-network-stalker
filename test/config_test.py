import unittest
from services import config

class ConfigTest(unittest.TestCase):

    config_service = config.Config()

    def test_get_twitter_account(self):

        twitter_account = self.config_service.get_twitter_account()
        self.assertEqual(twitter_account, "astrsnpy")

if __name__ == '__main__':
    unittest.main()