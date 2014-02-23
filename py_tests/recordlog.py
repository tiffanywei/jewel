import json
import unittest
from models.recordlog import RecordLog
import redis_client_for_testing

class TestRecordLog(unittest.TestCase):
  def setUp(self):
    self.test_redis = redis_client_for_testing.get_test_redis_client()

  def tearDown(self):
    self.test_redis.flushdb()
    
  def test_to_json(self):
    rl = RecordLog(2, 3, 1337, '"services"', None, self.test_redis)
    from_json = json.loads(rl.to_json())
    self.assertEqual(2, from_json['debtor'])
    self.assertEqual(3, from_json['creditor'])

  def test_store(self):
    rl = RecordLog(4, 5, 1337, '"services"', None, self.test_redis)
    rl.store()
    self.assertEqual(rl.to_json(), self.test_redis.get('RecordLog:1'))
    # TODO Verify that _link_user_pair stuff happened.
