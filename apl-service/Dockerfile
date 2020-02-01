FROM python:3.8

WORKDIR /usr/src/

RUN pip install requests flask

# Using COPY because "volumes" isn't able to use on FARGATE.
COPY ./src/server.py /usr/src/server.py 
COPY ./src/results.py /usr/src/results.py 

CMD python ./server.py
