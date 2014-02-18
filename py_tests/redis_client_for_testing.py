import redis
import subprocess

TEST_REDIS_PORT = 6479
TEST_RDB_FILE = 'test.rdb'

def get_test_redis_client():
  _start_test_redis_server()
  redis_url = 'redis://localhost:%d' % TEST_REDIS_PORT
  return redis.StrictRedis.from_url(redis_url)

def _start_test_redis_server():
  # TODO: Check redis binaries into git third-party directory instead of assuming that redis is installed globally.
  # TODO: Should the output of redis-server go to a log file?
  subprocess.call(['/usr/local/bin/redis-server',
      '--port', str(TEST_REDIS_PORT),
      '--daemonize', 'yes',
      # Don't persist data to disk for testing.
      '--save', '',
      # Probably don't need this because of save "", but we don't want to risk overwriting dump.rdb.
      '--dbfilename', TEST_RDB_FILE,
  ])
  
  
