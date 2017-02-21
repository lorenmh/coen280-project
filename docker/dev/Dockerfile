FROM ubuntu

RUN apt-get update && apt-get install -y build-essential \
  libpq-dev \
  postgresql-client \
  python3-dev \
  python3-setuptools \
  python3-psycopg2 \
  curl

RUN easy_install3 pip

WORKDIR /
ADD ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code

RUN ln -s /usr/bin/python3 /usr/bin/python
