import math
import random
import re
from collections.abc import Callable
from typing import Dict

from .circl import Circl, Point
from .program import main_program
from .interpreter import Environment

var_circl = Circl()  # TODO: Please find a better way to do this


class Identifier(Circl):
    def __hash__(self):
        return hash(str(self))


def _hash_circl_or_point(value: Circl | Point) -> int:
    return hash(Identifier([_hash_circl_or_point(v) for v in value]) if isinstance(value, Circl) else value)


def _apply_elementwise(environment: Environment, func: Callable[[Point,Point],Point]):
    arg2 = environment.main_circl.pop()
    arg1 = environment.main_circl.pop()

    match (arg1, arg2):
        case (Circl(), Circl()):
            result = Circl([func(a, b) for a, b in zip(arg1, arg2)])
        case (Circl(), _):
            result = Circl([func(a, arg2) for a in arg1])
        case (_, Circl()):
            result = Circl([func(arg1, b) for b in arg2])
        case _:
            result = func(arg1, arg2)

    return result

def c_halt(environment: Environment):
    while len(environment.main_circl) > 0:
        environment.main_circl.pop()


def c_read_input(environment: Environment):
    environment.main_circl.append(input())


def c_pi(environment: Environment):
    environment.main_circl.append(math.pi)


def c_e(environment: Environment):
    environment.main_circl.append(math.e)


def c_inf(environment: Environment):
    environment.main_circl.append(math.inf)


def c_duplicate(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    environment.main_circl.append(to_operate1)
    environment.main_circl.append(to_operate1)


def c_pop(environment: Environment):
    environment.main_circl.pop()


def c_cycle_back(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    to_operate3 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2)
    environment.main_circl.append(to_operate1)
    environment.main_circl.append(to_operate3)


def c_cycle_forward(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    to_operate3 = environment.main_circl.pop()
    environment.main_circl.append(to_operate1)
    environment.main_circl.append(to_operate3)
    environment.main_circl.append(to_operate2)


def c_swap_last(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate1)
    environment.main_circl.append(to_operate2)


def c_move_top(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    environment.main_circl.append(environment.main_circl[-to_operate1 + 1])


def c_println(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    # TODO: refactor stdout_copy such that circl doesnt store this information anymore. Maybe move to class Program?
    environment.main_circl.stdout_copy += str(to_operate1)
    print(to_operate1)


def c_print(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    # TODO: refactor stdout_copy such that circl doesnt store this information anymore. Maybe move to class Program?
    environment.main_circl.stdout_copy += str(to_operate1) + '\n'
    print(to_operate1, end="")


def c_read_file(environment: Environment):
    filename = environment.main_circl.pop()
    with open(filename, "r") as f:
        environment.main_circl.append(f.read())


def c_write_file(environment: Environment):
    filename = environment.main_circl.pop()
    to_operate1 = environment.main_circl.pop()
    with open(filename, "w") as f:
        f.write(to_operate1)


def c_length(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    environment.main_circl.append(len(to_operate1))


def c_radius(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(to_operate1.radius())
    else:
        environment.main_circl.append(len(to_operate1) / (2 * math.pi))


def c_cast_float(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([float(i) for i in to_operate1]))
    else:
        environment.main_circl.append(float(to_operate1))


def c_cast_int(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([int(i) for i in to_operate1]))
    else:
        environment.main_circl.append(int(to_operate1))


def c_to_precision(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([f"{i:.{to_operate2}f}" for i in to_operate1]))
    else:
        environment.main_circl.append(f"{to_operate1:.{to_operate2}f}")


def c_ordinal(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([ord(i) for i in to_operate1]))
    else:
        environment.main_circl.append(ord(to_operate1))


def c_cast_char(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([chr(i) for i in to_operate1]))
    else:
        environment.main_circl.append(chr(to_operate1))


def c_rnd(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(random.choice(to_operate1))
    else:
        if to_operate1 == 1:
            environment.main_circl.append(random.random())
        else:
            environment.main_circl.append(random.randint(0, to_operate1))


def c_logical_not(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([not i for i in to_operate1]))
    else:
        environment.main_circl.append(not to_operate1)


def c_logical_and(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a and b))



def c_logical_or(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a or b))


def c_logical_xor(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a ^ b))


def c_left_shift(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a << b))


def c_right_shift(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a >> b))


def c_equals(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate1 == to_operate2)


def c_not_equals(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate1 != to_operate2)


def c_lower_than(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2 < to_operate1)


def c_greater_than(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2 > to_operate1)


def c_lower_than_equal(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2 <= to_operate1)


def c_greater_than_equal(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2 >= to_operate1)


def c_jump_if_true(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if to_operate1:
        main_program.increment_counter(to_operate2)


def c_jump_if_false(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if not to_operate1:
        main_program.increment_counter(to_operate2)


def c_increment_program_counter_by(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    main_program.increment_counter(to_operate1)


def c_decrement_program_counter_by(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    main_program.decrement_counter(to_operate1 - 1)


def c_execute_as_circl(environment: Environment, exec_subroutine):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        exec_subroutine(to_operate1)
        environment.main_circl.stdout_copy += to_operate1.stdout_copy
    else:
        raise TypeError(f"Expected Circl, got {type(to_operate1)}")


def c_remove_nth_element(environment: Environment):
    n = environment.main_circl.pop()
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        items = to_operate1
        n = n % len(items) if items else 0
        environment.main_circl.append(Circl(items[n:] + items[:n]))
    else:
        n = n % len(to_operate1) if to_operate1 else 0
        environment.main_circl.append(to_operate1[n:] + to_operate1[:n])


def c_remove_negative_nth_element(environment: Environment):
    n = environment.main_circl.pop()
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        items = to_operate1
        n = n % len(items) if items else 0
        environment.main_circl.append(Circl(items[-n:] + items[:-n]) if n else Circl(items))
    else:
        n = n % len(to_operate1) if to_operate1 else 0
        environment.main_circl.append((to_operate1[-n:] + to_operate1[:-n]) if n else to_operate1)


def c_set_index_zero(environment: Environment):
    n = environment.main_circl.pop()
    length = len(environment.main_circl)
    n = n % length if length else 0
    items = environment.main_circl
    rotated = items[n:] + items[:n]
    while len(environment.main_circl) > 0:
        environment.main_circl.pop()
    for item in rotated:
        environment.main_circl.append(item)
    main_program.set_counter((main_program.get_counter() - n) % length - 1)


def c_append_range(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        # TODO: add step argument
        environment.main_circl.append(Circl([x for x in range(to_operate1[0], to_operate1[1])]))
    else:
        environment.main_circl.append(Circl([x for x in range(to_operate1)]))


def c_append_range_circl(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl(Circl(x for x in range(i)) for i in to_operate1))
    else:
        environment.main_circl.append(Circl(x for x in range(to_operate1)))


def c_square(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([i ** 2 for i in to_operate1]))
    else:
        environment.main_circl.append(to_operate1 ** 2)


def c_sqrt(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([i ** 0.5 for i in to_operate1]))
    else:
        environment.main_circl.append(to_operate1 ** 0.5)


def c_pow(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a ** b))


def c_floor(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.floor(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.floor(to_operate1))


def c_ceil(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.ceil(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.ceil(to_operate1))


def c_round(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([round(i) for i in to_operate1]))
    else:
        environment.main_circl.append(round(to_operate1))


# TODO: make this max over both operators
def c_max(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(max(to_operate1, key=lambda x: x))
    elif isinstance(to_operate2, Circl):
        environment.main_circl.append(max(to_operate2, key=lambda x: x))
    else:
        environment.main_circl.append(max(to_operate1, to_operate2))


# TODO: make this min over both operators
def c_min(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(min(to_operate1, key=lambda x: x))
    elif isinstance(to_operate2, Circl):
        environment.main_circl.append(min(to_operate2, key=lambda x: x))
    else:
        environment.main_circl.append(min(to_operate1, to_operate2))


def c_abs(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([abs(i) for i in to_operate1]))
    else:
        environment.main_circl.append(abs(to_operate1))


def c_logn(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.log(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.log(to_operate1))


def c_log10(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.log10(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.log10(to_operate1))


def c_sin(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.sin(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.sin(to_operate1))


def c_cos(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.cos(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.cos(to_operate1))


def c_tan(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([math.tan(i) for i in to_operate1]))
    else:
        environment.main_circl.append(math.tan(to_operate1))


def c_split(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([Circl(list(i)) for i in to_operate1]))
    else:
        environment.main_circl.append(Circl(list(to_operate1)))


def c_slice(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    to_operate3 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl(to_operate1[to_operate3:to_operate2]))
    else:
        environment.main_circl.append(to_operate1[to_operate3:to_operate2])


def c_replace_string(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    to_operate3 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl(
            [
                i.replace(to_operate3, to_operate2) if type(i) is str else i
                for i in to_operate1
            ]
        ))
    else:
        environment.main_circl.append(to_operate1.replace(to_operate3, to_operate2))


def c_uppercase(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([i.upper() for i in to_operate1]))
    else:
        environment.main_circl.append(to_operate1.upper())


def c_lowercase(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([i.lower() for i in to_operate1]))
    else:
        environment.main_circl.append(to_operate1.lower())


def c_sum(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(sum(i for i in to_operate1))
    else:
        environment.main_circl.append(to_operate1)


def c_product(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        result = 1.0
        for i in to_operate1:
            result *= i
        environment.main_circl.append(result)
    else:
        environment.main_circl.append(to_operate1)


def c_contains(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2 in to_operate1)


def c_not_contains(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(to_operate2 not in to_operate1)


def c_indexof(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(
            to_operate1.index(to_operate2) if to_operate2 in to_operate1 else "-1"
        )
    else:
        environment.main_circl.append(to_operate1.find(to_operate2))


def c_intersection(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl) and isinstance(to_operate2, Circl) is Circl:
        environment.main_circl.append(Circl([i for i in to_operate2 if i in set(to_operate1)]))
    elif isinstance(to_operate1, Circl) is Circl:
        environment.main_circl.append("".join(i for i in to_operate2 if i in set(to_operate1)))
    elif isinstance(to_operate2, Circl):
        environment.main_circl.append("".join(i for i in to_operate1 if i in set(to_operate2)))
    else:
        environment.main_circl.append("".join(i for i in to_operate2 if i in to_operate1))


def c_union(environment: Environment):
    to_operate2 = environment.main_circl.pop()
    to_operate1 = environment.main_circl.pop()

    circl1 = Circl(to_operate1)
    circl2 = Circl(to_operate2)

    seen = set()
    result = []

    for element in circl1 + circl2:
        if _hash_circl_or_point(element) not in seen:
            seen.add(_hash_circl_or_point(element))
            result.append(element)
    environment.main_circl.append(Circl(result))


def c_difference(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl) and isinstance(to_operate2, Circl):
        environment.main_circl.append(Circl([i for i in to_operate2 if i not in set(to_operate1)]))
    elif isinstance(to_operate1, Circl):
        environment.main_circl.append("".join(i for i in to_operate2 if i not in set(to_operate1)))
    elif isinstance(to_operate2, Circl):
        environment.main_circl.append(Circl([i for i in to_operate2 if i != to_operate1]))
    else:
        environment.main_circl.append("".join(i for i in to_operate2 if i not in to_operate1))


def c_zip(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: Circl([a, b])))


def c_stack_size(environment: Environment):
    environment.main_circl.append(len(environment.main_circl))


def c_sort(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(
            Circl(sorted(to_operate1, key=
            lambda x: (x if x.replace(".", "", 1).lstrip("-").isdigit() else x)))
        )
    else:
        environment.main_circl.append("".join(sorted(to_operate1)))


def c_reverse(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl(list(reversed(to_operate1))))
    else:
        environment.main_circl.append(to_operate1[::-1])


def c_replace(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    to_operate3 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        to_operate1[to_operate2] = to_operate3
        environment.main_circl.append(to_operate1)
    else:
        lst = list(to_operate1)
        lst[to_operate2] = to_operate3
        environment.main_circl.append("".join(lst))


def c_all_elements_equal(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        if to_operate1[1:] == to_operate1[:-1]:
            environment.main_circl.append(True)
        else:
            environment.main_circl.append(False)
    else:
        if list(to_operate1)[1:] == list(to_operate1)[:-1]:
            environment.main_circl.append(True)
        else:
            environment.main_circl.append(False)


def c_circlify(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    environment.main_circl.append(Circl(to_operate1))


def c_uncirclify(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        for i in to_operate1:
            environment.main_circl.append(i)


def c_str_join(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        if isinstance(to_operate2, Circl):
            new_elements = []
            base_list = to_operate1
            for separator in to_operate2:
                joined_str = separator.join(base_list)
                new_elements.append(Circl(joined_str))

            environment.main_circl.append(Circl(new_elements))
        else:
            environment.main_circl.append(to_operate2.join(to_operate1))
    else:
        if isinstance(to_operate2, Circl):
            environment.main_circl.append(to_operate1.join(to_operate2))
        else:
            environment.main_circl.append(to_operate2.join(list(to_operate1)))


def c_str_split(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        to_operate2 = environment.main_circl.pop()
        if isinstance(to_operate2, Circl):
            new = []
            for elem in to_operate2:
                new.append(Circl(i.split(elem) for i in to_operate1))
            environment.main_circl.append(Circl(new))
        else:
            environment.main_circl.append(Circl(i.split(to_operate2) for i in to_operate1))
    else:
        to_operate2 = environment.main_circl.pop()
        if isinstance(to_operate2, Circl):
            environment.main_circl.append(Circl(i.split(to_operate1) for i in to_operate2))
        else:
            environment.main_circl.append(Circl(to_operate1.split(to_operate2)))


def c_add_circl_elems(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a + b))

def c_sub_circl_elems(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a - b))

def c_mul_circl_elems(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a * b))

def c_div_circl_elems(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a / b))

def c_mod_circl_elems(environment: Environment):
    environment.main_circl.append(_apply_elementwise(environment, lambda a, b: a % b))




def c_negate(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(Circl([-i for i in to_operate1]))
    else:
        environment.main_circl.append(-to_operate1)


def c_extend(environment: Environment):
    to_operate2 = environment.main_circl.pop()
    to_operate1 = environment.main_circl.pop()

    match (to_operate1, to_operate2):
        case (Circl(), _) | (_, Circl()):
            environment.main_circl.append(Circl(Circl(to_operate1) + Circl(to_operate2)))
        case (str(), str()):
            environment.main_circl.append(to_operate1 + to_operate2)
        case (_, _):
            environment.main_circl.append(Circl(Circl(to_operate1) + Circl(to_operate2)))


def c_mul_circlify(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    environment.main_circl.append(Circl([to_operate2] * to_operate1))


def c_typeof(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    environment.main_circl.append(to_operate1)
    environment.main_circl.append("circl" if isinstance(to_operate1, Circl) else "string")


def c_unique(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        seen = []
        result = []
        for i in to_operate1:
            if i not in seen:
                seen.append(i)
                result.append(i)
        environment.main_circl.append(Circl(result))
    else:
        seen = []
        result = []
        for i in to_operate1:
            if i not in seen:
                seen.append(i)
                result.append(i)
        environment.main_circl.append("".join(result))


def c_circlify_multiple(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    items = []
    for i in range(to_operate1):
        items.append(environment.main_circl.pop())
    environment.main_circl.append(Circl(list(reversed(items))))


def c_append_program_counter(environment: Environment):
    environment.main_circl.append(main_program.get_counter())


def c_count(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        environment.main_circl.append(to_operate1.count(to_operate2))
    else:
        environment.main_circl.append(to_operate1.count(to_operate2))


def c_var_push(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    id_ = _hash_circl_or_point(to_operate1)
    for var in var_circl:
        if var[0] == id_:
            var[1] = to_operate2
            return
    var_circl.append(Circl([id_, to_operate2]))


def c_var_pull(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    looking = _hash_circl_or_point(to_operate1)
    for var in var_circl:
        if var[0] == looking:
            environment.main_circl.append(var[1])
            break


def c_var_del(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    id_ = _hash_circl_or_point(to_operate1)
    for i, var in enumerate(var_circl):
        if var[0] == id_:
            var_circl.pop(i)
            return


def c_regex_match(environment: Environment):
    to_operate1 = environment.main_circl.pop()
    to_operate2 = environment.main_circl.pop()
    if isinstance(to_operate1, Circl):
        if isinstance(to_operate2, Circl):
            new = []
            for elem in to_operate1:
                new.append(Circl([re.findall(elem, i) for i in to_operate2]))
            environment.main_circl.append(Circl(new))
        else:
            environment.main_circl.append(Circl([re.findall(i, to_operate2) for i in to_operate1]))
    else:
        if isinstance(to_operate2, Circl):
            environment.main_circl.append(Circl([re.findall(i, to_operate1) for i in to_operate2]))
        else:
            environment.main_circl.append(Circl(re.findall(to_operate1, to_operate2)))


# MAIN INSTRUCTION SET
# Each declared function above should correspond to a character (i.e. command)
class Instruction:
    def __init__(self, operation: Callable, calls_subroutine: bool = False) -> None:
        self.operation = operation
        self.calls_subroutine = calls_subroutine


instruction_set: Dict[str, Instruction] = {
    ".": Instruction(c_halt),
    "˅": Instruction(c_read_input),
    "π": Instruction(c_pi),
    "ε": Instruction(c_e),
    "∞": Instruction(c_inf),
    "⧺": Instruction(c_duplicate),
    "↓": Instruction(c_pop),
    "↶": Instruction(c_cycle_back),
    "↷": Instruction(c_cycle_forward),
    "⇄": Instruction(c_swap_last),
    "@": Instruction(c_move_top),
    "^": Instruction(c_println),
    "§": Instruction(c_print),
    "←": Instruction(c_read_file),
    "→": Instruction(c_write_file),
    "⇀": Instruction(c_length),
    "⦰": Instruction(c_radius),
    "♯": Instruction(c_cast_float),
    "♭": Instruction(c_cast_int),
    "Φ": Instruction(c_to_precision),
    "Ψ": Instruction(c_ordinal),
    "Ω": Instruction(c_cast_char),
    "⚂": Instruction(c_rnd),
    "¬": Instruction(c_logical_not),
    "∧": Instruction(c_logical_and),
    "∨": Instruction(c_logical_or),
    "⊕": Instruction(c_logical_xor),
    "⋘": Instruction(c_left_shift),
    "⋙": Instruction(c_right_shift),
    "=": Instruction(c_equals),
    "≠": Instruction(c_not_equals),
    "<": Instruction(c_lower_than),
    ">": Instruction(c_greater_than),
    "≤": Instruction(c_lower_than_equal),
    "≥": Instruction(c_greater_than_equal),
    "⁇": Instruction(c_jump_if_true),
    "‽": Instruction(c_jump_if_false),
    "⇒": Instruction(c_increment_program_counter_by),
    "⇐": Instruction(c_decrement_program_counter_by),
    "↺": Instruction(c_execute_as_circl, calls_subroutine=True),
    "⊲": Instruction(c_remove_nth_element),
    "⊳": Instruction(c_remove_negative_nth_element),
    "⊙": Instruction(c_set_index_zero),
    "⡳": Instruction(c_append_range),
    "⇡": Instruction(c_append_range_circl),
    "²": Instruction(c_square),
    "√": Instruction(c_sqrt),
    "ⁿ": Instruction(c_pow),
    "⌊": Instruction(c_floor),
    "⌈": Instruction(c_ceil),
    "○": Instruction(c_round),
    "⌃": Instruction(c_max),
    "⌄": Instruction(c_min),
    "|": Instruction(c_abs),
    "ℓ": Instruction(c_logn),
    "ℒ": Instruction(c_log10),
    "∿": Instruction(c_sin),
    "⌒": Instruction(c_cos),
    "∡": Instruction(c_tan),
    "✄": Instruction(c_split),
    "⊂": Instruction(c_slice),
    "↔": Instruction(c_replace_string),
    "⬆": Instruction(c_uppercase),
    "⬇": Instruction(c_lowercase),
    "∑": Instruction(c_sum),
    "Π": Instruction(c_product),
    "∈": Instruction(c_contains),
    "∉": Instruction(c_not_contains),
    "⍳": Instruction(c_indexof),
    "∩": Instruction(c_intersection),
    "∪": Instruction(c_union),
    "⊖": Instruction(c_difference),
    "⊛": Instruction(c_zip),
    "⌀": Instruction(c_stack_size),
    "κ": Instruction(c_sort),
    "ρ": Instruction(c_reverse),
    "χ": Instruction(c_replace),
    "≡": Instruction(c_all_elements_equal),
    "‾": Instruction(c_circlify),
    "_": Instruction(c_uncirclify),
    "⋃": Instruction(c_str_join),
    "✂": Instruction(c_str_split),
    "+": Instruction(c_add_circl_elems),
    "-": Instruction(c_sub_circl_elems),
    "×": Instruction(c_mul_circl_elems),
    "÷": Instruction(c_div_circl_elems),
    "%": Instruction(c_mod_circl_elems),
    "⁻": Instruction(c_negate),
    "∥": Instruction(c_extend),
    "⊡": Instruction(c_mul_circlify),
    "τ": Instruction(c_typeof),
    "⌂": Instruction(c_unique),
    "⊤": Instruction(c_circlify_multiple),
    "⊞": Instruction(c_append_program_counter),
    "ν": Instruction(c_count),
    "↦": Instruction(c_var_push),
    "↤": Instruction(c_var_pull),
    "🜏": Instruction(c_var_del),
    "Я": Instruction(c_regex_match)
}
