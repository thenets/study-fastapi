import pytest

@pytest.skip("Not implemented")
def test_root(session_fastapi_client, is_json):
    response = session_fastapi_client.get("/")
    assert response.status_code == 200, "Response status is %d" % response.status_code
    assert is_json(response.content), "Response is not JSON"

def test_item_get(session_fastapi_client, is_json, load_json):
    response = session_fastapi_client.get("/items/0")
    assert response.status_code == 200, "Response status is %d" % response.status_code
    assert is_json(response.content), "Response is not JSON"

    data = load_json(response.content)
    assert data["item_name"] == "Foo", "Item Name is %d" % data["item_name"]

