# Third-party imports...
from unittest.mock import patch

# Local imports...
from services import get_users
from tests.mocks import get_free_port, start_mock_server

class TestMockServer(object):
    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_request_response(self):
        mock_users_url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('services.__dict__', {'USERS_URL': mock_users_url}):
            response = get_users()

        assert 'Content-Type' in response.headers.keys()
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert response.ok, True
        assert response.json() == []