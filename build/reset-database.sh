#!/bin/bash
cd ${0%/*}/..
DROP_CREATE_STR="$(cat build/sql/drop_db.sql) $(cat build/sql/create_db.sql)"
echo "$DROP_CREATE_STR" | PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -h $DB_HOST -w $DB_NAME_DEFAULT
