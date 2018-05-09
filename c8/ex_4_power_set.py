import unittest

def get_powerset(s: set) -> set:
    powerset = set()
    powerset.add(frozenset(s))
    _get_powerset(s, powerset)
    return powerset


def _get_powerset(s: set, subsets: set):
    if not s:
        return set()

    for e in s:
        subset = s.difference({e})
        subsets.add(frozenset(subset))
        _get_powerset(subset, subsets)


class MyTestCase(unittest.TestCase):
    def test_powerset(self):
        self.set = {1, 2, 3}
        self.power_set = [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
        print(get_powerset(self.set))
        self.assertEqual(get_powerset(self.set), set(frozenset(i) for i in self.power_set))


if __name__ == '__main__':
    unittest.main()
