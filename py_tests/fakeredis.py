

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
    self.state.setdefault(key, set())
    sorted_set = self.state[key]
    sorted_set_element = _new_sorted_set_element(score, member)
    sorted_set.add(sorted_set_element)

  def zrange(self, key, start, stop, with_scores=False):
    sorted_set = self.state[key]
    elements = sorted(sorted_set)
    if with_scores:
      raise 'not implemented'
    else:
      return [element.split(_SCORE_MEMBER_SEPARATOR)[1] for element in elements[start:stop]]

_SCORE_MEMBER_SEPARATOR = '___'
def _new_sorted_set_element(score, member):
  return '%s%s%s' % (score, _SCORE_MEMBER_SEPARATOR, member)
