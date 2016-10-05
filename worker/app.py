import os
from redis import StrictRedis
from rq import Connection, Worker

# use the kubernetes service environment variables to 
#  connect to the redis queue

REDIS_HOST =  os.environ['REDIS_MASTER_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_MASTER_SERVICE_PORT']
REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
QUEUES = ['default']

#connection=StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

def runworker():
  redis_connection = redis.from_url(REDIS_URL)
  with Connection(redis_connection):
    worker = Worker(QUEUES)
    worker.work()

if __name__ == '__main__':
  runworker()

