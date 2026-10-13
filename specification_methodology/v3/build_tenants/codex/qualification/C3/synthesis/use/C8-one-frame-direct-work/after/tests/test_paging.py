from utils.paging import page_count


def test_exact():
    assert page_count(20, 10) == 2


def test_empty():
    assert page_count(0, 10) == 0


def test_partial_last_page():
    # Regression for issue 9: a partial final page must be counted.
    assert page_count(11, 10) == 2


def test_less_than_one_page():
    assert page_count(1, 10) == 1
