import pytest

from circl import Circl, c_lowercase, c_replace_string, c_uppercase


def test_lowercase_requires_strings_in_circl():
    stack = Circl([Circl(["ABC", 1])])

    with pytest.raises(TypeError, match="Expected str"):
        c_lowercase(stack)


def test_uppercase_accepts_strings_in_circl():
    stack = Circl([Circl(["ab", "cd"])])

    c_uppercase(stack)

    assert stack.pop() == Circl(["AB", "CD"])


def test_replace_string_requires_string_operands():
    stack = Circl(["a", "b", 1])

    with pytest.raises(TypeError, match="Expected str"):
        c_replace_string(stack)
