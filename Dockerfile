FROM python:3.9.16-slim-buster

COPY requirements.txt .
COPY break_snowflake.py .

# python housekeeping
RUN pip install --upgrade pip wheel setuptools && pip install -r requirements.txt
ENV PYTHONFAULTHANDLER=1

ENTRYPOINT [ "python break_snowflake.py" ]
