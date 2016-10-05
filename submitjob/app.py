import os
import random 
import randtest
from redis import StrictRedis
from rq import Queue

# use the kubernetes service environment variables to 
#  connect to the redis queue

REDIS_HOST =  os.environ['REDIS_MASTER_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_MASTER_SERVICE_PORT']
q = Queue(connection=StrictRedis(host=REDIS_HOST, port=REDIS_PORT))


tests={1:'monobitfrequencytest',\
       2:'blockfrequencytest',\
       3:'runstest',\
       4:'longestrunones10000',
       5:'binarymatrixranktest',\
       6:'spectraltest',\
       7:'nonoverlappingtemplatematchingtest',\
       8:'overlappingtemplatematchingtest',\
       9:'maurersuniversalstatistictest',\
       10:'linearcomplexitytest',\
       11:'serialtest',\
       12:'aproximateentropytest',\
       13:'cumultativesumstest',\
       14:'randomexcursionstest',\
       15:'randomexcursionsvarianttest',\
       16:'cumultativesumstestreverse',\
       17:'lempelzivcompressiontest'\
      }

def add_job(inputbits):
  for i in tests:
    job = q.enqueue(eval("randtest."+tests.get(i), inputbits, result_ttl=5000)


if __name__ == '__main__':
  inputbits = random.getrandbits(1000000)
  add_job(inputbits)
