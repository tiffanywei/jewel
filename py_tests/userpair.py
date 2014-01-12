import unittest
from models.userpair import UserPair
from fakeredis import FakeRedis

class TestUserPair(unittest.TestCase):
  def setUp(self):
    self.fake_redis = FakeRedis()

  def test_add(self):
    up = UserPair('vlad', 'tiffy', self.fake_redis)
    up.add('RecordLog:1', 0)
    self.assertTrue('UserPair:tiffy:vlad' in self.fake_redis.state)
    self.assertTrue('0___RecordLog:1' in self.fake_redis.state['UserPair:tiffy:vlad'])
