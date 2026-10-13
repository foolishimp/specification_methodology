def page_count(total, per_page):
    if per_page <= 0:
        raise ValueError('per_page must be positive')
    return -(-total // per_page)
