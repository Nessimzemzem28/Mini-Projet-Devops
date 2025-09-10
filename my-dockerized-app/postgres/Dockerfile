FROM postgres:17

ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

COPY initdb/init.sql /docker-entrypoint-initdb.d/