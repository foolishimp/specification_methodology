def remove_last(entries):
    items = list(entries)
    count = len(items)
    items.pop()
    return items, count
