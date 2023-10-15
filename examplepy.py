# This function is to find the maximum element and change places with the element on 0 position
def sweep_max(items: list) -> list:
    max_pos = items.index(max(items))
    items[0], items[max_pos] = items[max_pos], items[0]
    return items


items = [0, 8, 10, 2, 20, 10]
result = sweep_max(items)
print(result)
