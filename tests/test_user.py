import pytest
import requests
import responses

print("Starting test script")

@responses.activate
def test_unauthorized_access():
    print("Running test_unauthorized_access")
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    full_url = f"{url}?username=admin&password=admin"
    responses.add(responses.GET, full_url, status=401, body='')

    response = requests.get(url, params=params)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    assert response.text == '', f"Expected empty response, but got {response.text}"

if __name__ == "__main__":
    print("Running pytest")
    pytest.main()
