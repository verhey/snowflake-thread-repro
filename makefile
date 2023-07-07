image:=break-snowflake

build:
	docker build . -t $(image)

test:
	docker run \
	-e SNOWSQL_USER=$${SNOWSQL_USER} -e SNOWSQL_PWD=$${SNOWSQL_PWD} -e SNOWSQL_ACCOUNT=$${SNOWSQL_ACCOUNT} \
	$(image):latest

copy-logs:
	docker cp $$(docker container ls --latest --quiet):/python_connector.log ./python_connector_$$(date +"%I:%M:%S").log
	docker logs $$(docker container ls --latest --quiet) > stdout_$$(date +"%I:%M:%S").log 2>&1
