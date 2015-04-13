from redis_client import get_redis

class UserPair(object):
  """
  Read and modify RecordLogs associated with a given pair of users.

  There is no need to construct this class in order to add RecordLogs to it.
  See Recordlog#get_user_pair() and RecordLog#store().
  """
  @staticmethod
  def make_key(user1_key, user2_key):
    return 'UserPair:%s:%s' % tuple(
        # To generate predictable UserPair keys for any pair of user IDs,
        # sort the user IDs. This way we know that all record involving
        # user 4 and user 3 will be associated with key UserPair:3:4.
        sorted((user1_key, user2_key)))

  def __init__(self, user1_key, user2_key, redis_client=None):
    self._redis = get_redis() if redis_client is None else redis_client
    self.userpair_key = UserPair.make_key(user1_key, user2_key)

  def redis_add_record_log(self, recordlog_key, timestamp):
    self._redis.zadd(self.userpair_key, timestamp, recordlog_key)

  def redis_get_record_logs(self, start=0, stop=10):
    return self._redis.zrange(self.userpair_key, start, stop)

  def __eq__(self, other):
    return self.userpair_key == other.userpair_key

  def __ne__(self, other):
    return not self.__eq__(other)
