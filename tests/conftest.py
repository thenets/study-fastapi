import sys

sys.path.append("../src")

import pytest
import json
from fastapi.testclient import TestClient
from src import main

@pytest.fixture(scope="session")
def session_main():
    return main


@pytest.fixture(scope="session")
def session_fastapi_client():
    return TestClient(main.app)


@pytest.fixture(scope="function")
def load_json():
    def f_load_json(data:str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON") 

    return f_load_json

@pytest.fixture(scope="function")
def is_json():
    def f_is_json(data:str):
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False

    return f_is_json