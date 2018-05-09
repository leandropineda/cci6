"""
INPUT   Tact Coa
Output  True (permutations: "taco cat", "atco cta", etc)
"""


def _string_to_dict(_input: str) -> dict:
    _output_mapping = dict()
    for i in _input:
        _output_mapping[i] = _output_mapping.get(i, 0) + 1
    return _output_mapping


def is_permutation_palindrome(_input: str) -> bool:
    string = _input.lower()
    dict_mapping = _string_to_dict(string)
    char_counters = dict_mapping.values()
    if sum(char_counters) % 2:
        return False
    return True