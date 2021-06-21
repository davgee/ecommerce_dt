FROM python:3

WORKDIR /ecommerce_dt
COPY requirements.txt /ecommerce_dt/requirements.txt
RUN pip install -r /ecommerce_dt/requirements.txt

COPY src /ecommerce_dt/src
COPY Makefile /ecommerce_dt/Makefile
COPY alembic /ecommerce_dt/alembic
COPY alembic.ini /ecommerce_dt/alembic.ini
COPY wait-for-it.sh /ecommerce_dt/wait-for-it.sh

