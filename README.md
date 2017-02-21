# COEN281 - PROJECT

## TODO / OVERVIEW
We will want:

* ORM models corresponding to the data we want to store. We should probably use SQLAlchemy
* A component which fetches data from the reddit API, rate limited (1 req/sec max), this component needs to insert rows (using the defined ORM models)
* A component which performs the analysis / clustering based on data in the DB

## INSTALL INSTRUCTIONS
Install docker and docker-compose.
Clone this repository.
Then, simply run `docker-compose up` and the images and everything should automagically work.

To run a bash shell of the development image, run `./scripts/dev/bash.sh`.
To run the postgresql shell, run `./scripts/psql/psql.sh`, or to run the bash shell of the postgresql image, run `./scripts/psql/bash.sh`, though this probably won't be necessary.

# Docker images
Docker will have the binaries / programs required to run everything. Docker is not necessary, but keep in mind you'll need to install PostgreSQL (or whatever DB we use) natively, as well as all other dependencies (like a psql driver for python).

I will be putting the docker image up onto dockerhub under lorenmh/dev.

If you don't want to use docker, you'll want to use Python virtualenv.
