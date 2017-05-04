import unittest
from services import twitter

class TwitterTest(unittest.TestCase):

    twitter_service = twitter.Twitter()

    def test_get_twitter_data_from_account(self):
        twitter_data = self.twitter_service.get_twitter_data_from_account()
        self.assertEqual("twitter_count" in twitter_data, True)

if __name__ == '__main__':
    unittest.main()