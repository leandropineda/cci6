"""
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def string_edits(_string1: str, _string2: str) -> bool:
    _string_list1 = list(_string1)
    _string_list2 = list(_string2)
    len_diff = len(_string_list1) - len(_string_list2)
    if len_diff == 1:  # remove char
        diff = list()
        for i in range(len(_string_list2)):
            if _string_list1[i] != _string_list2[i]:
                diff.append(_string_list1[i])
                _string_list1.pop(i)
        if len(diff) > 1:
            return False
    if len_diff == -1:  # add char
        diff = list()
        for i in range(len(_string_list1)):
            if _string_list1[i] != _string_list2[i]:
                diff.append(_string_list2[i])
                _string_list2.pop(i)
        if len(diff) > 1:
            return False
    if len_diff == 0:  # replace char
        diff = list()
        for i in range(len(_string_list1)):
            if _string_list1[i] != _string_list2[i]:
                diff.append(_string_list2[i])
        if len(diff) > 1:
            return False
    return True
