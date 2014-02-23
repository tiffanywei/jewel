from redis_client import get_redis
import json
import time
from userpair import UserPair
from userpairsforuser import UserPairsForUser


class RecordLog(object):
  """
  This class tracks creditor and debtor because though UserPairs know both of these uers,
  they don't know the transaction type (lent or borrowed).

  key is randomly generated UUID
  value is a json string
  
  <record_log_key>: {
    creditor: <user_key>,
    debtor: <user_key>,
    timestamp: <int>
    amount: <float>
    memo: <string>
  }
  """

  @staticmethod
  def _new_key(redis_client):
    next_key = redis_client.incr('RecordLogCount')
    return 'RecordLog:%s' % next_key

  def __init__(self, debtor_key, creditor_key, amount, memo=None, timestamp=None, redis_client=None):
    self._redis = get_redis() if redis_client is None else redis_client

    self.debtor_key = debtor_key
    self.creditor_key = creditor_key
    self.amount = amount
    self.memo = memo or ''
    self.timestamp = timestamp or time.time()

  def store(self):
    """
    Associate this RecordLog to a UserPair and store it in redis.
    """
    key = RecordLog._new_key(self._redis)
    self._redis.set(key, self.to_json())
    user_pair = self.get_user_pair()
    user_pair.add_record_log(key, self.timestamp)
    self._link_user_pair()

  def to_json(self):
    return json.dumps({
      'debtor': self.debtor_key,
      'creditor': self.creditor_key,
      'amount': self.amount,
      'memo': self.memo,
      'time': self.timestamp
    })

  def get_user_pair(self):
    return UserPair(self.debtor_key, self.creditor_key, self._redis)

  def _link_user_pair(self):
    upfu1 = UserPairsForUser(self.creditor_key, self._redis)
    upfu2 = UserPairsForUser(self.debtor_key, self._redis)
    upfu1.add_secondary_user(self.debtor_key)
    upfu2.add_secondary_user(self.creditor_key)
