class TestUserPairsForUser(unittest.TestCase):
  def setUp(self):
    self.fake_redis = FakeRedis()

  def test_add_secondary_user(self):
    upfu = UserPairsForUser('primary tiffany', self.fake_redis)
    upfu.add_secondary_user('secondary vlad', 0)
    # TODO: assert
