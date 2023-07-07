import logging
import os
import threading

from dotenv import load_dotenv

from snowflake import connector


def connect_to_snowflake(thread_num: int) -> connector.SnowflakeConnection:
    print(f"Starting thread {thread_num}")
    return connector.connect(
        user=os.getenv("SNOWSQL_USER"),
        password=os.getenv("SNOWSQL_PWD"),
        account="hs00696.us-east-1",
        role="SNOWFLAKE_ENGINEERING",
        warehouse="XSMALL_WH",
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

    for i in range(20):
        thread = threading.Thread(target=connect_to_snowflake, args=(i,))
        thread.start()


if __name__ == "__main__":
    main()
