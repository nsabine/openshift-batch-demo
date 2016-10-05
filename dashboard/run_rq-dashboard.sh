#!/bin/bash

rq-dashboard --port 9181 --redis-host $REDIS_MASTER_SERVICE_HOST --redis-port $REDIS_MASTER_SERVICE_HOST
