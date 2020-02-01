FROM python:3.6

WORKDIR /usr/src/

RUN pip install flask mysql-connector-python

COPY ./src/server.py /usr/src/server.py 
COPY ./src/students.py /usr/src/students.py 

CMD python ./server.py
