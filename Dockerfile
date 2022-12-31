FROM postgres:12

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB newspapers

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
