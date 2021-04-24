run:
	. venv/bin/activate && \
		uvicorn main:app --reload

fmt:
	. venv/bin/activate && \
		black .

create-venv:
	virtualenv -p python3 venv
	. venv/bin/activate && \
		pip install -r requirements.txt

services-start:
	docker run -d --rm \
		--name redis \
		-p 6379:6379 \
		redis

services-stop:
	docker stop redis
