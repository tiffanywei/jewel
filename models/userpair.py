from redis_client import get_redis

class UserPair(object):
  @staticmethod
  def make_key(debtor_key, creditor_key):
    return 'UserPair:%s:%s' % tuple(sorted((debtor_key, creditor_key)))

  def __init__(self, debtor_key, creditor_key):
    self.key = UserPair.make_key(debtor_key, creditor_key)

  def add(self, key, timestamp):
    get_redis().zadd(self.key, key, timestamp)

  def get_record_logs(self, start=0, stop=10):
    return get_redis().zrange(self.key, start, stop)
