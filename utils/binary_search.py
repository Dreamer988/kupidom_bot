def binary_search(array, search_value: str):
    left_point = 0
    right_point = len(array)
    middle_point = int((right_point + left_point) / 2)
    while right_point - 1 > left_point:
        if str(search_value) == str(array[middle_point]):
            return middle_point
        elif str(search_value) < str(array[middle_point]):
            right_point = middle_point
            middle_point = int((right_point + left_point) / 2)
        elif str(search_value) > str(array[middle_point]):
            left_point = middle_point
            middle_point = int((right_point + left_point) / 2)
    return False
