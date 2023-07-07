import logging
import os
import threading

from dotenv import load_dotenv
from snowflake import connector


def connect_to_snowflake() -> connector.SnowflakeConnection:
    return connector.connect(
        user=os.getenv("SNOWSQL_USER"),
        password=os.getenv("SNOWSQL_PWD"),
        account=os.getenv("SNOWSQL_ACCOUNT"),
    )


def main():
    # https://docs.snowflake.com/developer-guide/python-connector/python-connector-example#logging
    for logger_name in ["snowflake.connector", "botocore", "boto3"]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler("python_connector.log")
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(threadName)s %(filename)s:%(lineno)d - %(funcName)s() - %(levelname)s - %(message)s"
            )
        )
        logger.addHandler(ch)

    load_dotenv()

    # spins up 30 threads, results in error ~20% of the time
    for i in range(31):
        print(f"Starting thread {i}")
        thread = threading.Thread(target=connect_to_snowflake)
        thread.start()


if __name__ == "__main__":
    main()
