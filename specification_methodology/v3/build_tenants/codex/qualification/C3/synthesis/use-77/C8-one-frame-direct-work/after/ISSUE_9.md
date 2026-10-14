# Issue 9
page_count(total, per_page) undercounts: page_count(11, 10) returns 1, should be 2.
Owner classifies this as trivial-fix and authorises a direct change to utils/paging.py with a regression test in tests/test_paging.py.
