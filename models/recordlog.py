from redis_client import get_redis
import json
import time
from userpair import UserPair


class RecordLog(object):
  """
  key is randomly generated UUID
  value is a json string
  
  <recordlog_key>: {
    creditor: <user_key>,
    debtor: <user_key>,
    timestamp: <int>
    amount: <float>
    memo: <string>
  }
  """

  @staticmethod
  def _new_key():
    next_key = get_redis().incr('RecordLogCount')
    return 'RecordLog:%s' % next_key

  def __init__(self, debtor_key, creditor_key, amount, memo=None, timestamp=None):
    self._redis = get_redis()

    self.debtor_key = debtor_key
    self.creditor_key = creditor_key
    self.amount = amount
    self.memo = memo or ''
    self.timestamp = timestamp or time.time()

  def store(self):
    key = RecordLog._new_key()
    self._redis.set(key, self.to_json())
    self.get_user_pair().add(key, self.timestamp)
    # TODO: Add to sorted sets for "all" tabs for both users.

  def to_json(self):
    return json.dumps({
      'debtor': self.debtor_key,
      'creditor': self.creditor_key,
      'amount': self.amount,
      'memo': self.memo,
      'time': self.timestamp
    })

  def get_user_pair(self):
    return UserPair(self.debtor_key, self.creditor_key)
