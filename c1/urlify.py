"""
INPUT   "Mr John Smith     ", 13
OUTPUT  "Mr%20John%20Smith"
"""


def urlify(_input: str, _real_length: int) -> str:
    replace_str = '%20'
    url = _input[0:_real_length].replace(' ', replace_str)
    return url
