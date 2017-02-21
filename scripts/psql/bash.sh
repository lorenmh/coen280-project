#!/bin/bash
cd ${0%/*}/../..
docker-compose exec postgresql /bin/bash
