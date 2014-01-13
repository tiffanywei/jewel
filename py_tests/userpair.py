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

  def test_get_record_logs(self):
    up = UserPair('vlad', 'tiffy', self.fake_redis)
    up.add('RecordLog:3', 2)
    up.add('RecordLog:1', 0)
    up.add('RecordLog:2', 1)
    record_logs = up.get_record_logs( 0, 3)
    self.assertEquals(['RecordLog:1', 'RecordLog:2', 'RecordLog:3'], record_logs)
    record_logs = up.get_record_logs(0)
    self.assertEquals(['RecordLog:1', 'RecordLog:2', 'RecordLog:3'], record_logs)
    record_logs = up.get_record_logs()
    self.assertEquals(['RecordLog:1', 'RecordLog:2', 'RecordLog:3'], record_logs)
