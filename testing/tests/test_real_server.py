from unittest import skipIf

# Local imports...
from constants import SKIP_TAGS
from services import get_users

@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
def test_request_response():
    response = get_users()

    assert 'Content-Type' in response.headers.keys()
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.ok, True
    assert isinstance(response.json(), list)