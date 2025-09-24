import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

def test_initial_balance_negative_raises():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-50)


def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150


def test_deposit2(start_account):
    with pytest.raises(ValueError):
        start_account.deposit(0)
        


    
def test_withdraw_positive():
    account=BankAccount(100)
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        account.withdraw(-5)
    
def test_withdraw_insufficient_funds_raises():
    account = BankAccount(50)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(100)

def test_withdraw():
    account=BankAccount(100)
    account.withdraw(50)


def test_transfer_valid():
    acc1 = BankAccount(100)
    acc2 = BankAccount(50)
    acc1.transfer_to(acc2, 40)
    assert acc1.balance == 60
    assert acc2.balance == 90



def test_transfer_invalid_target():
    acc1 = BankAccount(100)
    with pytest.raises(ValueError, match="Target must be a BankAccount"):
        acc1.transfer_to("not an account", 50)
