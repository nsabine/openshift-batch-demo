import os

REDIS_HOST =  os.environ['REDIS_MASTER_SERVICE_HOST']
REDIS_PORT =  os.environ['REDIS_MASTER_SERVICE_PORT']
QUEUES = ['default']
REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

