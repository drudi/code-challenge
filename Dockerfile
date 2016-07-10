FROM ubuntu:14.04
MAINTAINER Marcelo Drudi Miranda <mdrudi@gmail.com>

RUN apt-get update && apt-get install -y python3 python3-pip python3-dev && apt-get clean

RUN pip3 install gunicorn
RUN pip3 install gevent
RUN pip3 install bottle
RUN pip3 install voluptuous

EXPOSE 8000

ADD . /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "1", "-k", "gevent", "--log-file", "-", "--log-level", "debug", "--access-logfile", "-", "--chdir", "spotippos",  "run:app"]
