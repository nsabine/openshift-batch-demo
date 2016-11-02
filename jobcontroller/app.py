import os
import argparse
from redis import StrictRedis
from rq import Queue

# use the kubernetes service environment variables to 
#  connect to the redis queue

REDIS_HOST =  os.environ['REDIS_MASTER_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_MASTER_SERVICE_PORT']
# REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# QUEUES = ['default']

redis_conn = StrictRedis(host=os.environ['REDIS_MASTER_SERVICE_HOST'], 
                 port=os.environ['REDIS_MASTER_SERVICE_PORT'], db=0)
redis_queue = Queue(queue_name, connection=redis_conn)

def populate_queue():
  # todo

def create_workers(name, image):
  # Accessing the API using the pod's service account
  # $ TOKEN="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"
  # $ curl --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
  #            "https://openshift.default.svc.cluster.local/oapi/v1/users/~" \
  #                -H "Authorization: Bearer $TOKEN"

  # todo: 
  #  - create job for each message in the queue

def monitor_batch():
  # todo
  #  - monitor for failures?  retry?

def gather_result():
  # todo

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Manage Batch Job')
  parser.add_argument('--name', help='unique job name (used for queue name)')
  parser.add_argument('--image', help='worker image')
  parser.add_argument('--dir', help='working directory')
  parser.add_argument('--exe', help='executable')

  args = parser.parse_args()
  
  populate_queue()
  create_workers(args.name, args.image)
  monitor_batch()
  gather_result()
