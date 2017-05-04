import unittest
from services import twitter

class TwitterTest(unittest.TestCase):

    twitter_service = twitter.Twitter()

    def test_get_twitter_data_from_account(self):

        self.assertEqual("test", "test")

if __name__ == '__main__':
    unittest.main()