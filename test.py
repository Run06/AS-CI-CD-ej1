from wallet import Wallet

def test_getbalance():
    obj = Wallet(0)
    obj.add_1000()
    assert obj.get_balance() == 1000
