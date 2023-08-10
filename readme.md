# Update 2023-08

This issue has since been fixed by Snowflake, and connector versions >= 3.1.0 do not experience this segfault

# snowflake-thread-repro

Attempt to repro the segfault error described in snowflakedb/snowflake-connector-python/issues/1627

## Prerequisites

* A snowflake account and username/password auth
* Docker

## Setup

1. Clone the repo, ideally spin up a virtualenv
2. Install requirements `pip install -r requirements.txt`
3. Build the image `make build`
4. Create a `.env` file and fill it out with your info - `cp sample.env .env`
5. Run the test script to try and repro the bug - `make test` - the test script just spins up a bunch of threads and snowflake connections and does nothing else
6. You'll probably need to run it a few times to get the error to occur, but when it does you'll see a stack trace in `stdout` from your container.
7. When the error occurs, capture the logs with `make copy-logs`
