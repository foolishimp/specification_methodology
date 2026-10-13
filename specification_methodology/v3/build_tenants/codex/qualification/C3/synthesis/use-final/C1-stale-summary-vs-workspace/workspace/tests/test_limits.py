from src.limits import MAX_ITEMS, MAX_BATCH

def test_limits():
    assert MAX_ITEMS == 50
    assert MAX_BATCH == 10
