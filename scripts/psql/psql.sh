#!/bin/bash
cd ${0%/*}/../..
# using run for right now because the proc isnt long running
docker-compose exec postgresql /bin/bash -c 'PGPASSWORD=password psql -U user -w local'
