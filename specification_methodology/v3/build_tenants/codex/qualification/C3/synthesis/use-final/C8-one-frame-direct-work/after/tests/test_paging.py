from utils.paging import page_count


def test_exact():
    assert page_count(20, 10) == 2


def test_empty():
    assert page_count(0, 10) == 0


def test_partial_page():
    assert page_count(11, 10) == 2
    assert page_count(1, 10) == 1
