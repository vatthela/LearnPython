import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def wallet100():
	return Wallet(100)