#!/bin/bash
cd ${0%/*}/../..
docker-compose exec postgresql /bin/bash -c 'PGPASSWORD=password psql -U user -w local'
