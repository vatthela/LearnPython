# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.mark.ini
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

@pytest.mark.ini
def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet100 = Wallet(100)
    wallet100.spend_cash(10)
    assert wallet100.balance == 90

# def test_wallet_spend_cash_again():
#     wallet100 = Wallet(100)
#     wallet.spend_cash(10)
#     assert wallet.balance == 90

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet100 = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet100.spend_cash(100)

# @pytest.fixture
# def empty_wallet():
#     '''Returns a Wallet instance with a zero balance'''
#     return Wallet()

# @pytest.fixture
# def wallet20():
#     '''Returns a Wallet instance with a balance of 20'''
#     return Wallet(20)

# @pytest.mark.parametrize("earned,spent,expected", [
#     (30, 10, 20),
#     (20, 2, 18),
# ])
# def test_params(earned, spent, expected):
#     my_wallet = Wallet()
#     my_wallet.add_cash(earned)
#     my_wallet.spend_cash(spent)
#     assert my_wallet.balance == expected

# Kết hợp fixture và parametrize
# @pytest.mark.parametrize("earned,spent,expected", [
#     (30, 10, 120),
#     (20, 2, 118),
# ])
# def test_transactions(wallet100, earned, spent, expected):
#     wallet100.add_cash(earned)
#     wallet100.spend_cash(spent)
#     assert wallet100.balance == expected
