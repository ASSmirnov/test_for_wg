from unittest import TestCase
from main import is_string_reducible


fixture = [
    ("XYYX", True),
    ("XYZYX", False),
    ("XXZWWZZZXYY", True),
    ("AAABBACCCAAB", True),
    ("AAABBACCCAABC", False),
    ("ABBACCCAAB", False),
    ("ABBACCCAABB", True),
]


class Test(TestCase):

    def test_use_case(self):
        for string, result in fixture:
            assert is_string_reducible(string) == result

