# COEN281 - PROJECT

We will want:

* ORM models corresponding to the data we want to store. We should probably use SQLAlchemy
* A component which fetches data from the reddit API, rate limited (1 req/sec max), this component needs to insert rows (using the defined ORM models)
* A component which performs the analysis / clustering based on data in the DB

# Docker images
Docker will have the binaries / programs required to run everything. Docker is not necessary, but keep in mind you'll need to install PostgreSQL (or whatever DB we use) natively, as well as all other dependencies (like a psql driver for python).

I will be putting the docker image up onto dockerhub under lorenmh/dev.

If you don't want to use docker, you'll want to use Python virtualenv.
