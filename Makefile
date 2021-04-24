run:
	. venv/bin/activate && uvicorn main:app --reload

create-venv:
	virtualenv -p python3 venv
	. venv/bin/activate && pip install -r requirements.txt
