import pytest
import requests
from unittest.mock import Mock, patch
from services import get_todos, get_uncompleted_todos

# 3
@pytest.mark.step3
def test_request_response():
    # 1
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    # response = get_todos()

    # Confirm that the request-response cycle completed successfully.
    assert response.ok, True

# 4
@pytest.mark.step4
@patch('services.requests.get')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response != None

# 5
@pytest.mark.step5
def test_getting_todos_with_context_manager():
    with patch('services.requests.get') as mock_get:
        mock_get.return_value.ok = True

        # Call the service, which will send a request to the server.
        response = get_todos()
    assert response != None

#6
@pytest.mark.step6
def test_another_getting_todos():
    mock_get_patcher = patch('services.requests.get')

    # Start patching `requests.get`.
    mock_get = mock_get_patcher.start()
    mock_get.return_value.ok = True

    response = get_todos()

    mock_get_patcher.stop()

    assert response != None

# 7
@pytest.mark.step7
@patch('services.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    # request.get() trả ra một đối tượng Response
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response.json() == todos

@pytest.mark.step7
@patch('services.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    mock_get.return_value.ok = False
    response = get_todos()
    assert (response is None)

# 8
@pytest.mark.step8
@patch('services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_not_none(mock_get_todos):
    todo1 = {
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }
    todo2 = {
        'userId': 1,
        'id': 2,
        'title': 'Walk the dog',
        'completed': True
    }

    # Configure mock to return a response with a JSON-serialized list of todos.
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = [todo1, todo2]

    uncompleted_todos = get_uncompleted_todos()
    assert mock_get_todos.called, True

    # Confirm that the expected filtered list of todos was returned.
    assert uncompleted_todos == [todo1]

@pytest.mark.step8
@patch('services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_none(mock_get_todos):
    mock_get_todos.return_value = None
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert mock_get_todos.called, True

    # Confirm that an empty list was returned.
    assert uncompleted_todos == []
