FROM mysql/mysql-server:5.7

COPY ./db/mysql_init/setup.sql /docker-entrypoint-initdb.d/setup.sql

RUN chown -R mysql /var/lib/mysql && \
    chgrp -R mysql /var/lib/mysql

