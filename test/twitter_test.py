import unittest
from services import twitter

class TwitterTest(unittest.TestCase):

    twitter_service = twitter.Twitter()

    def test_get_twitter_data_from_account(self):
        twitter_data = self.twitter_service.get_twitter_data_from_account()
        self.assertEqual("tweets_count" in twitter_data, True)
        self.assertEqual("following_count" in twitter_data, True)
        self.assertEqual("followers_count" in twitter_data, True)
        self.assertEqual("likes_count" in twitter_data, True)

if __name__ == '__main__':
    unittest.main()