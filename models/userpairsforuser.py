import time
from models.userpair import UserPair

class UserPairsForUser(object):
  """
  Read and modify the sorted set of secondary users associated with a given primary user.
  """

  def _make_key(self):
    return 'PrimaryUser:' + self._primary_user

  def __init__(self, primary_user, redis_client=None):
    self._redis = get_redis() if redis_client is None else redis_client
    self._primary_user = primary_user
    self._user_pairs_for_user_key = self._make_key()

  def add_secondary_user(self, secondary_user, timestamp=None):
    timestamp = timestamp or time.time()
    self._redis.zadd(self._user_pairs_for_user_key, timestamp, secondary_user)

  def get_user_pairs(self):
    secondary_users = self._redis.zrange(self._user_pairs_for_user_key, 0, -1)
    user_pairs_by_secondary_user = {}
    for secondary_user in secondary_users:
      user_pairs_by_secondary_user[secondary_user] = UserPair(self._primary_user, secondary_user, self._redis)
    return user_pairs_by_secondary_user


    
