# COEN281 - PROJECT

## TODO / OVERVIEW
We will want:

* ORM models corresponding to the data we want to store. We should probably use
  SQLAlchemy
* A component which fetches data from the reddit API, rate limited (1 req/sec
  max), this component needs to insert rows (using the defined ORM models)
* A component which performs the analysis / clustering based on data in the DB

## INSTALL INSTRUCTIONS
1. Install docker and docker-compose.
2. Clone this repository.
3. Run `docker-compose up` in the repository directory. This will start the
   docker postgres container and the dev container.
4. Once these are running, you can test to make sure things are working by
   running ipython from within the dev container. To test this, in a
   *different* shell (a different shell from the one where where
   `docker-compose up` is running), run `./scripts/dev/ipython.sh`. You should
   now see a python3 ipython repl; this is running from within the dev
   container.  You will be able to access all of the dev dependencies from this
   shell.

To run a bash shell of the development image, run `./scripts/dev/bash.sh`.

To run the postgresql shell, run `./scripts/psql/psql.sh`, or to run the bash
shell of the postgresql image, run `./scripts/psql/bash.sh`, though this
probably won't be necessary.

## DIRECTORIES
* `/code/` The project directory is mounted here, it is also the working dir from within the container
* `build/` this is where scripts/files go which are run from _within the container_
* `scripts/` this is where scripts/files go which are run from _outside the container_
* `src/` is where the source code for the python code will go

## Docker images
Docker will have the binaries / programs required to run everything. Docker is
not necessary, but keep in mind you'll need to install PostgreSQL (or whatever
DB we use) natively, as well as all other dependencies (like a psql driver for
python).

[Here's a link to the docker hub repository for the
image](https://hub.docker.com/r/lorenmh/coen281-project/).

If you don't want to use docker, you'll want to use Python virtualenv, you will
need to set this up yourself though.

# Style guidelines
Let's use flake8 style guidelines? Install the flake8 linter and it will let
you know what should be changed.
