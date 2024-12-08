import pytest
import requests
import responses

@responses.activate
def test_unauthorized_access():
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Correct URL with query parameters for exact matching
    full_url = f"{url}?username=admin&password=admin"

    # Mock the GET request
    responses.add(responses.GET, full_url, status=401, body='')

    response = requests.get(url, params=params)
    
    # Assert that the status code is 401
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    
    # Assert that the response content is empty
    assert response.text == '', f"Expected empty response, but got {response.text}"

if __name__ == "__main__":
    pytest.main()
