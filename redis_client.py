import redis
import os

def get_redis():
  redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
  return redis.StrictRedis.from_url(redis_url)
