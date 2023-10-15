# This function is to find the maximum element and change places with the element on 0 position
def sweep_max(items: list) -> list:
    max_item = items[0]
    max_pos = 0
    for i in range(len(items)):
        if max_item <= items[i]:
            max_item = items[i]
            max_pos = i
    items[max_pos] = items[0]
    items[0] = max_item
    return items


items = [0, 8, 10, 2, 20, 10]
result = sweep_max(items)
print(result)
