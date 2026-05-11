import builtins
from collections.abc import Iterator
from .circl import Circl

class Peekable[T]:
    def __init__(self, iter: Iterator[T]):
        self.iter = iter
        self.peeked = None

    def peek(self) -> T | None:
        match self.peeked:
            case None:
                self.peeked = builtins.next(self.iter, None)
                return self.peeked
            case next:
                return next

    def next(self) -> T | None:
        match self.peeked:
            case None:
                return builtins.next(self.iter, None)
            case next:
                self.peeked = None
                return next

def parse(input: str) -> Circl:
    input = Peekable(enumerate(input))
    circl = parse_circl(input)
    assert input.next() is None
    return circl

def parse_circl(input: Peekable[tuple[int, str]]) -> Circl:
    circl = Circl([])
    while True:
        next = input.peek()
        if next is None:
            break
        _, char = next
        match char:
            case ')':
                break
            case '\\':
                input.next()
                next = input.next()
                assert next is not None
                _, char = next
                circl.append(char)
            case '(':
                input.next()
                sub_circl = parse_subcircl(input)
                circl.append(sub_circl)
            case '#':
                input.next()
                number = parse_number(input)
                circl.append(number)
            case '"':
                input.next()
                string = parse_string(input)
                circl.append(string)
            case c:
                input.next()
                circl.append(c)
    return circl

def parse_subcircl(input: Peekable[tuple[int, str]]) -> Circl:
    sub_circl = parse_circl(input)
    next = input.next()
    assert next is not None
    _, char = next
    assert char == ')'
    return sub_circl


def parse_number(input: Peekable[tuple[int, str]]) -> int | float:
    number = []
    while True:
        next = input.next()
        assert next is not None
        _, char = next
        if char == '#':
            break
        number.append(char)
    number = ''.join(number)
    try:
        try_int = int(number)
        return try_int
    except:
        return float(number)

def parse_string(input: Peekable[tuple[int, str]]) -> str:
    string = []
    while True:
        next = input.next()
        assert next is not None
        _, char = next
        if char == '"':
            break
        string.append(char)
    return ''.join(string)