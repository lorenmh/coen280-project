#!/bin/bash
cd ${0%/*}/..
# docker-compose exec dev /bin/bash -c './build/reset-database.sh'
docker-compose exec dev bash -c './build/reset-database.sh'
