import json
import unittest
from models.recordlog import RecordLog
from fakeredis import FakeRedis

class TestRecordLog(unittest.TestCase):
  def setUp(self):
    self.fake_redis = FakeRedis()
    
  def test_to_json(self):
    rl = RecordLog(2, 3, 1337, '"services"', None, self.fake_redis)
    from_json = json.loads(rl.to_json())
    self.assertEqual(2, from_json['debtor'])
    self.assertEqual(3, from_json['creditor'])

  def test_store(self):
    rl = RecordLog(4, 5, 1337, '"services"', None, self.fake_redis)
    rl.store()
    self.assertEqual(rl.to_json(), self.fake_redis.state['RecordLog:1']) 
