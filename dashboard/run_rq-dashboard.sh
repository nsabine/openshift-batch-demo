#!/bin/bash

export LC_ALL=en_US.utf8
export LANG=en_US.utf8

rq-dashboard --port 9181 --redis-host $REDIS_MASTER_SERVICE_HOST --redis-port $REDIS_MASTER_SERVICE_HOST
