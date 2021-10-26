# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL

TODOS_URL = urljoin(BASE_URL, 'todos')
USERS_URL = urljoin(BASE_URL, 'users')

def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None

def get_uncompleted_todos():
    # pass
    response = get_todos()
    if response is None:
        return []
    else:
        todos = response.json()
        return [todo for todo in todos if todo.get('completed') == False]

def get_users():
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None