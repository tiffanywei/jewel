import unittest
import redis_client_for_testing
from models.userpairsforuser import UserPairsForUser
from models.userpair import UserPair

class TestUserPairsForUser(unittest.TestCase):
  def setUp(self):
    self.test_redis = redis_client_for_testing.get_test_redis_client()

  def tearDown(self):
    self.test_redis.flushdb()
    
  def test_redis_add_secondary_user(self):
    PRIMARY = 'primary tiffany'
    SECONDARY = 'secondary vlad'

    upfu = UserPairsForUser(PRIMARY, self.test_redis)
    upfu.redis_add_secondary_user(SECONDARY)
    secondary_user = self.test_redis.zrange('PrimaryUser:%s' % PRIMARY, 0, -1)[0]
    self.assertEquals(SECONDARY, secondary_user)

  def test_redis_get_user_pairs(self):
    PRIMARY = 'primary godzilla'
    SECONDARY = 'secondary husky'
    SECONDARY1 = 'secondary little husky'

    upfu = UserPairsForUser(PRIMARY, self.test_redis)
    upfu.redis_add_secondary_user(SECONDARY)
    upfu.redis_add_secondary_user(SECONDARY1)
    EXPECTED_USER_PAIRS = {
      SECONDARY: UserPair(PRIMARY, SECONDARY, self.test_redis),
      SECONDARY1: UserPair(PRIMARY, SECONDARY1, self.test_redis),
    }
    self.assertEquals(EXPECTED_USER_PAIRS, upfu.redis_get_user_pairs())
