

class FakeRedis(object):
  def __init__(self):
    # list of key, value pairs that were set()
    self.state = {}

  def set(self, key, value):
    self.state[key] = value

  def incr(self, key):
    self.state.setdefault(key, 0)
    self.state[key] += 1
    return self.state[key]

  def zadd(self, key, score, member):
    # Approximate SortedSet using specially keyed dicts.
    self.state.setdefault(key, {})
    sorted_set = self.state[key]
    sorted_set_key = _new_sorted_set_key(score, member)
    sorted_set[sorted_set_key] = True

  def zrange(self, key, start, stop, with_scores=False):
    sorted_set = self.state[key]
    keys = sorted(sorted_set.keys())
    if with_scores:
      raise 'not implemented'
    else:
      return [key.split(_SCORE_MEMBER_SEPARATOR)[1] for key in keys[start:stop]]

_SCORE_MEMBER_SEPARATOR = '___'
def _new_sorted_set_key(score, member):
  return '%s%s%s' % (score, _SCORE_MEMBER_SEPARATOR, member)
