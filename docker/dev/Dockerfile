FROM ubuntu

RUN apt-get update && apt-get install -y build-essential \
  libpq-dev \
  postgresql-client \
  python-psycopg2 \
  python-dev \
  python-setuptools \
  curl

RUN easy_install pip

WORKDIR /
ADD ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
