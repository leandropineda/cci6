from typing import List
from math import floor

def _get_idx_split(arr) -> int:
    return int(floor(len(arr)/2.0))


def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    merged_arr = list()
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            merged_arr.append(arr1.pop(0))
        else:
            merged_arr.append(arr2.pop(0))

    for i in arr1:
        merged_arr.append(i)
    for i in arr2:
        merged_arr.append(i)

    return merged_arr


def _merge_sort(arr) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid_idx = _get_idx_split(arr)
    arr1 = _merge_sort(arr[0: mid_idx])
    arr2 = _merge_sort(arr[mid_idx:])
    return merge(arr1, arr2)


def merge_sort(arr: List[int]) -> List[int]:
    return _merge_sort(arr)
