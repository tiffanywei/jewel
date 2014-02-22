import unittest
import redis_client_for_testing
from models.userpair import UserPair

class TestUserPair(unittest.TestCase):
  def setUp(self):
    self.test_redis = redis_client_for_testing.get_test_redis_client()

  def tearDown(self):
    self.test_redis.flushdb()
    
  def assertSortedSetContainsAll(self, key, expected_elements):
    elements = self.test_redis.zrange(key, 0, -1)
    self.assertEquals(expected_elements, elements)

  def test_add_record_log(self):
    up = UserPair(3, 4, self.test_redis)
    record_log_key = 'RecordLog:1'
    up.add_record_log(record_log_key, 0)
    self.assertSortedSetContainsAll(up.userpair_key, [record_log_key])

  def test_get_record_logs(self):
    up = UserPair(5, 6, self.test_redis)
    up.add_record_log('RecordLog:3', 2)
    up.add_record_log('RecordLog:1', 0)
    up.add_record_log('RecordLog:2', 1)
    record_logs = up.get_record_logs( 0, 3)
    self.assertEquals(['RecordLog:1', 'RecordLog:2', 'RecordLog:3'], record_logs)
    record_logs = up.get_record_logs(0)
    self.assertEquals(['RecordLog:1', 'RecordLog:2', 'RecordLog:3'], record_logs)
    record_logs = up.get_record_logs()
    self.assertEquals(['RecordLog:1', 'RecordLog:2', 'RecordLog:3'], record_logs)
