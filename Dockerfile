FROM python:3.9.16-slim-buster

COPY requirements.txt .
COPY break_snowflake.py .

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y --no-install-recommends git build-essential

# python housekeeping
RUN pip install --upgrade pip wheel setuptools && pip install -r requirements.txt
ENV PYTHONFAULTHANDLER=1

CMD ["python3", "break_snowflake.py"]
