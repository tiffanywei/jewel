from redis_client import get_redis

class UserPair(object):
  """
  Read and modify RecordLogs associated with a given pair of users.
  """
  @staticmethod
  def make_key(debtor_key, creditor_key):
    return 'UserPair:%s:%s' % tuple(
        # To generate predictable UserPair keys for any pair of user IDs,
        # sort the user IDs. This way we know that all record involving
        # user 4 and user 3 will be associated with key UserPair:3:4.
        sorted((debtor_key, creditor_key)))

  def __init__(self, debtor_key, creditor_key, redis_client=None):
    self._redis = get_redis() if redis_client is None else redis_client
    self.userpair_key = UserPair.make_key(debtor_key, creditor_key)

  def add_record_log(self, recordlog_key, timestamp):
    self._redis.zadd(self.userpair_key, timestamp, recordlog_key)

  def get_record_logs(self, start=0, stop=10):
    return self._redis.zrange(self.userpair_key, start, stop)
