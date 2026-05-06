import math, random
from typing import Dict, Callable

from Circl import Circl
from Program import Program


def c_halt(main_circl: Circl, main_program: Program):
    while len(main_circl) > 0:
        main_circl.pop()


def c_read_input(main_circl: Circl, main_program: Program):
    main_circl.append(input())


def c_pi(main_circl: Circl, main_program: Program):
    main_circl.append(str(math.pi))


def c_e(main_circl: Circl, main_program: Program):
    main_circl.append(str(math.e))


def c_inf(main_circl: Circl, main_program: Program):
    main_circl.append(str(math.inf))


def c_duplicate(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_circl.append(to_operate1)
    main_circl.append(to_operate1)


def c_pop(main_circl: Circl, main_program: Program):
    main_circl.pop()


def c_cycle_back(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    to_operate3 = main_circl.pop()
    main_circl.append(to_operate2)
    main_circl.append(to_operate1)
    main_circl.append(to_operate3)


def c_cycle_forward(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    to_operate3 = main_circl.pop()
    main_circl.append(to_operate1)
    main_circl.append(to_operate3)
    main_circl.append(to_operate2)


def c_swap_last(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    main_circl.append(to_operate1)
    main_circl.append(to_operate2)


def c_move_top(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_circl.append(main_circl.access(-(int(float(to_operate1)) + 1)))


def c_println(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    print(to_operate1)


def c_print(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    print(to_operate1, end="")


def c_read_file(main_circl: Circl, main_program: Program):
    filename = main_circl.pop()
    with open(filename, "r") as f:
        main_circl.append(f.read())


def c_write_file(main_circl: Circl, main_program: Program):
    filename = main_circl.pop()
    to_operate1 = main_circl.pop()
    with open(filename, "w") as f:
        f.write(str(to_operate1))


def c_length(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_circl.append(str(len(to_operate1)))


def c_radius(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(str(to_operate1.radius()))
    else:
        main_circl.append(str(len(to_operate1) / (2 * math.pi)))


def c_cast_float(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(float(i)) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(float(to_operate1)))


def c_cast_int(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(int(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(int(float(to_operate1))))


def c_to_precision(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    precision = int(float(to_operate2))
    if type(to_operate1) is Circl:
        main_circl.append(Circl([f"{float(i):.{precision}f}" for i in to_operate1.whole_list()]))
    else:
        main_circl.append(f"{float(to_operate1):.{precision}f}")


def c_ordinal(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(ord(i)) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(ord(to_operate1)))


def c_cast_char(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(chr(int(float(i)))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(chr(int(float(to_operate1)))))


def c_rnd(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(random.choice(to_operate1.whole_list()))
    else:
        if to_operate1 == "1":
            main_circl.append(str(random.random()))
        else:
            main_circl.append(str(random.randint(0, int(float(to_operate1)))))


def c_logical_not(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl(["1" if not float(i) else "0" for i in to_operate1.whole_list()]))
    else:
        main_circl.append("1" if not float(to_operate1) else "0")


def c_conjoin(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl([str("1" if float(a) and float(b) else "0") for a, b in
                                 zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(
            Circl(["1" if float(to_operate2) and float(i) else "0" for i in to_operate1.whole_list()]))
    elif type(to_operate2) is Circl:
        main_circl.append(
            Circl(["1" if float(i) and float(to_operate1) else "0" for i in to_operate2.whole_list()]))
    else:
        main_circl.append("1" if float(to_operate1) and float(to_operate2) else "0")


def c_disjoin(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl([str("1" if float(a) or float(b) else "0") for a, b in
                                 zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(
            Circl(["1" if float(to_operate2) or float(i) else "0" for i in to_operate1.whole_list()]))
    elif type(to_operate2) is Circl:
        main_circl.append(
            Circl(["1" if float(i) or float(to_operate1) else "0" for i in to_operate2.whole_list()]))
    else:
        main_circl.append("1" if float(to_operate1) or float(to_operate2) else "0")


def c_logical_xor(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl([str(int(float(a)) ^ int(float(b))) for a, b in
                                 zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(
            Circl([str(int(float(to_operate2)) ^ int(float(i))) for i in to_operate1.whole_list()]))
    elif type(to_operate2) is Circl:
        main_circl.append(
            Circl([str(int(float(i)) ^ int(float(to_operate1))) for i in to_operate2.whole_list()]))
    else:
        main_circl.append(str(int(float(to_operate1)) ^ int(float(to_operate2))))


def c_left_shift(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl([str(int(float(a)) << int(float(b))) for a, b in
                                 zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(
            Circl([str(int(float(to_operate2)) << int(float(i))) for i in to_operate1.whole_list()]))
    elif type(to_operate2) is Circl:
        main_circl.append(
            Circl([str(int(float(i)) << int(float(to_operate1))) for i in to_operate2.whole_list()]))
    else:
        main_circl.append(str(int(float(to_operate2)) << int(float(to_operate1))))


def c_right_shift(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl([str(int(float(a)) >> int(float(b))) for a, b in
                                 zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(
            Circl([str(int(float(to_operate2)) >> int(float(i))) for i in to_operate1.whole_list()]))
    elif type(to_operate2) is Circl:
        main_circl.append(
            Circl([str(int(float(i)) >> int(float(to_operate1))) for i in to_operate2.whole_list()]))
    else:
        main_circl.append(str(int(float(to_operate2)) >> int(float(to_operate1))))


def c_equals(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append("1" if to_operate1.whole_list() == to_operate2.whole_list() else "0")
    else:
        main_circl.append("1" if to_operate1 == to_operate2 else "0")


def c_not_equals(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append("0" if to_operate1.whole_list() == to_operate2.whole_list() else "1")
    else:
        main_circl.append("0" if to_operate1 == to_operate2 else "1")


def c_lower_than(main_circl: Circl, main_program: Program):
    # TODO: circls?
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    main_circl.append("1" if float(to_operate2) < float(to_operate1) else "0")


def c_greater_than(main_circl: Circl, main_program: Program):
    # TODO: circls?
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    main_circl.append("1" if float(to_operate2) > float(to_operate1) else "0")


def c_lower_than_equal(main_circl: Circl, main_program: Program):
    # TODO: circls?
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    main_circl.append("1" if float(to_operate2) <= float(to_operate1) else "0")


def c_greater_than_equal(main_circl: Circl, main_program: Program):
    # TODO: circls?
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    main_circl.append("1" if float(to_operate2) >= float(to_operate1) else "0")


def c_truthy_program_counter_increment(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if not float(to_operate1):
        main_program.counter += int(float(to_operate2))


def c_falsy_program_counter_increment(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if float(to_operate1):
        main_program.counter += int(float(to_operate2))


def c_increment_program_counter_by(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_program.counter += int(float(to_operate1))


def c_decrement_program_counter_by(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_program.counter = int(float(to_operate1)) - 1


def c_execute_as_circl(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        execute(to_operate1)


def c_remove_nth_element(main_circl: Circl, main_program: Program):
    n = int(float(main_circl.pop()))
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        items = to_operate1.whole_list()
        n = n % len(items) if items else 0
        main_circl.append(Circl(items[n:] + items[:n]))
    else:
        n = n % len(to_operate1) if to_operate1 else 0
        main_circl.append(to_operate1[n:] + to_operate1[:n])


def c_remove_negative_nth_element(main_circl: Circl, main_program: Program):
    n = int(float(main_circl.pop()))
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        items = to_operate1.whole_list()
        n = n % len(items) if items else 0
        main_circl.append(Circl(items[-n:] + items[:-n]) if n else Circl(items))
    else:
        n = n % len(to_operate1) if to_operate1 else 0
        main_circl.append((to_operate1[-n:] + to_operate1[:-n]) if n else to_operate1)


def c_set_index_zero(main_circl: Circl, main_program: Program):
    n = int(float(main_circl.pop()))
    length = len(main_circl)
    n = n % length if length else 0
    items = main_circl.whole_list()
    rotated = items[n:] + items[:n]
    while len(main_circl) > 0:
        main_circl.pop()
    for item in rotated:
        main_circl.append(item)
    main_program.counter = (main_program.counter - n) % length - 1


def c_append_range(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        # TODO: add step argument
        main_circl.append(Circl([str(x) for x in range(int(float(to_operate1.whole_list()[0])),
                                                       int(float(to_operate1.whole_list()[1])))]))
    else:
        main_circl.append(Circl([str(x) for x in range(int(float(to_operate1)))]))


def c_append_range_circl(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(
            Circl(Circl(str(x) for x in range(int(float(i)))) for i in to_operate1.whole_list()))
    else:
        main_circl.append(Circl(str(x) for x in range(int(float(to_operate1)))))


def c_square(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(float(i) ** 2) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(float(to_operate1) ** 2))


def c_sqrt(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(float(i) ** 0.5) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(float(to_operate1) ** 0.5))


def c_pow(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl(
            [str(float(a) ** float(b)) for a, b in zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(Circl([str(float(to_operate2) ** float(i)) for i in to_operate1.whole_list()]))
    elif type(to_operate2) is Circl:
        main_circl.append(Circl([str(float(i) ** float(to_operate1)) for i in to_operate2.whole_list()]))
    else:
        main_circl.append(str(float(to_operate2) ** float(to_operate1)))


def c_floor(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.floor(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.floor(float(to_operate1))))


def c_ceil(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.ceil(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.ceil(float(to_operate1))))


def c_round(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(round(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(round(float(to_operate1))))


#TODO: make this max over both operators
def c_max(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(max(to_operate1.whole_list(), key=lambda x: float(x)))
    elif type(to_operate2) is Circl:
        main_circl.append(max(to_operate2.whole_list(), key=lambda x: float(x)))
    else:
        main_circl.append(str(max(float(to_operate1), float(to_operate2))))


#TODO: make this min over both operators
def c_min(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(min(to_operate1.whole_list(), key=lambda x: float(x)))
    elif type(to_operate2) is Circl:
        main_circl.append(min(to_operate2.whole_list(), key=lambda x: float(x)))
    else:
        main_circl.append(str(min(float(to_operate1), float(to_operate2))))


def c_abs(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(abs(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(abs(float(to_operate1))))


def c_logn(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.log(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.log(float(to_operate1))))


def c_log10(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.log10(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.log10(float(to_operate1))))


def c_sin(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.sin(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.sin(float(to_operate1))))


def c_cos(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.cos(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.cos(float(to_operate1))))


def c_tan(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(math.tan(float(i))) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(math.tan(float(to_operate1))))


def c_split(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([Circl(list(i)) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(Circl(list(to_operate1)))


def c_inclusion(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    to_operate3 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl(to_operate1.whole_list()[int(float(to_operate3)):int(float(to_operate2))]))
    else:
        main_circl.append(to_operate1[int(float(to_operate3)):int(float(to_operate2))])


def c_unknown1(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    to_operate3 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([i.replace(to_operate3, to_operate2) if type(i) is str else i for i in
                                 to_operate1.whole_list()]))
    else:
        main_circl.append(to_operate1.replace(to_operate3, to_operate2))


def c_uppercase(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([i.upper() for i in to_operate1.whole_list()]))
    else:
        main_circl.append(to_operate1.upper())


def c_lowercase(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([i.lower() for i in to_operate1.whole_list()]))
    else:
        main_circl.append(to_operate1.lower())


def c_sum(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(str(sum(float(i) for i in to_operate1.whole_list())))
    else:
        main_circl.append(to_operate1)


def c_mul(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        result = 1.0
        for i in to_operate1.whole_list():
            result *= float(i)
        main_circl.append(str(result))
    else:
        main_circl.append(to_operate1)


def c_contains(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append("1" if to_operate2 in to_operate1.whole_list() else "0")
    else:
        main_circl.append("1" if to_operate2 in to_operate1 else "0")


def c_not_contains(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append("1" if to_operate2 not in to_operate1.whole_list() else "0")
    else:
        main_circl.append("1" if to_operate2 not in to_operate1 else "0")


def c_indexof(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        lst = list(to_operate1)
        main_circl.append(str(lst.index(to_operate2)) if to_operate2 in to_operate1.whole_list() else "-1")
    else:
        main_circl.append(str(to_operate1.find(to_operate2)))


def c_join(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl([i for i in to_operate2.whole_list() if i in set(to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append("".join(i for i in to_operate2 if i in set(to_operate1.whole_list())))
    elif type(to_operate2) is Circl:
        main_circl.append("".join(i for i in to_operate1 if i in set(to_operate2.whole_list())))
    else:
        main_circl.append("".join(i for i in to_operate2 if i in to_operate1))


def c_union(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        seen = set()
        result = []
        for i in to_operate2.whole_list() + to_operate1.whole_list():
            if i not in seen:
                seen.add(i)
                result.append(i)
        main_circl.append(Circl(result))
    else:
        seen = set()
        result = []
        for i in to_operate2 if type(to_operate2) is str else "".join(
                to_operate2.whole_list()) + to_operate1 if type(to_operate1) is str else "".join(
            to_operate1.whole_list()):
            if i not in seen:
                seen.add(i)
                result.append(i)
        main_circl.append("".join(result))


def c_disjunctive_union(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(
            Circl([i for i in to_operate2.whole_list() if i not in set(to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append("".join(i for i in to_operate2 if i not in set(to_operate1.whole_list())))
    elif type(to_operate2) is Circl:
        main_circl.append(Circl([i for i in to_operate2.whole_list() if i != to_operate1]))
    else:
        main_circl.append("".join(i for i in to_operate2 if i not in to_operate1))


def c_unknown_instruction1(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(
            Circl([Circl([a, b]) for a, b in zip(to_operate2.whole_list(), to_operate1.whole_list())]))
    elif type(to_operate1) is Circl:
        main_circl.append(
            Circl([Circl([a, b]) for a, b in zip(list(to_operate2), to_operate1.whole_list())]))
    elif type(to_operate2) is Circl:
        main_circl.append(
            Circl([Circl([a, b]) for a, b in zip(to_operate2.whole_list(), list(to_operate1))]))
    else:
        main_circl.append(Circl([Circl([a, b]) for a, b in zip(list(to_operate2), list(to_operate1))]))


def c_unknown_instruction2(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        items = to_operate1.whole_list()
        main_circl.append(
            Circl([str(float(items[i + 1]) - float(items[i])) for i in range(len(items) - 1)]))
    else:
        main_circl.append(to_operate1)


def c_this_length(main_circl: Circl, main_program: Program):
    main_circl.append(str(len(main_circl)))


def c_unknown_instruction3(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl(sorted(to_operate1.whole_list(),
                                       key=lambda x: float(x) if x.replace('.', '', 1).lstrip(
                                           '-').isdigit() else x)))
    else:
        main_circl.append("".join(sorted(to_operate1)))


def c_reverse(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl(list(reversed(to_operate1.whole_list()))))
    else:
        main_circl.append(to_operate1[::-1])


def c_unknown_instruction4(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    to_operate3 = main_circl.pop()
    if type(to_operate1) is Circl:
        to_operate1.set(int(float(to_operate2)), to_operate3)
        main_circl.append(to_operate1)
    else:
        lst = list(to_operate1)
        lst[int(float(to_operate2))] = to_operate3
        main_circl.append("".join(lst))


def c_equivalent(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        if to_operate1.whole_list()[1:] == to_operate1.whole_list()[:-1]:
            main_circl.append("1")
        else:
            main_circl.append("0")
    else:
        if list(to_operate1)[1:] == list(to_operate1)[:-1]:
            main_circl.append("1")
        else:
            main_circl.append("0")


def c_circlify(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_circl.append(Circl(to_operate1))


def c_add_all(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        for i in to_operate1.whole_list():
            main_circl.append(i)


def c_unknown_instruction5(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        if type(to_operate2) is Circl:
            new_elements = []
            base_list = to_operate1.whole_list()
            for separator in to_operate2.whole_list():
                joined_str = separator.join(base_list)
                new_elements.append(Circl(joined_str))

            main_circl.append(Circl(new_elements))
        else:
            main_circl.append(to_operate2.join(to_operate1.whole_list()))
    else:
        if type(to_operate2) is Circl:
            main_circl.append(to_operate1.join(to_operate2.whole_list()))
        else:
            main_circl.append(to_operate2.join(list(to_operate1)))


def c_split_circlify(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        to_operate2 = main_circl.pop()
        if type(to_operate2) is Circl:
            new = []
            for elem in to_operate2.whole_list():
                new.append(Circl(i.split(elem) for i in to_operate1.whole_list()))
            main_circl.append(Circl(new))
        else:
            main_circl.append(Circl(i.split(to_operate2) for i in to_operate1.whole_list()))
    else:
        to_operate2 = main_circl.pop()
        if type(to_operate2) is Circl:
            main_circl.append(Circl(i.split(to_operate1) for i in to_operate2.whole_list()))
        else:
            main_circl.append(Circl(to_operate1.split(to_operate2)))


def c_add_circl_elems(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        if type(to_operate2) is Circl:
            new = []
            for elem in to_operate1.whole_list():
                new.append(Circl([str(float(i) + float(elem)) for i in to_operate2.whole_list()]))
            main_circl.append(Circl(new))
        else:
            main_circl.append(Circl([str(float(to_operate2) + float(i)) for i in to_operate1.whole_list()]))
    else:
        if type(to_operate2) is Circl:
            main_circl.append(Circl([str(float(to_operate1) + float(i)) for i in to_operate2.whole_list()]))
        else:
            main_circl.append(str(float(to_operate1) + float(to_operate2)))


def c_sub_circl_elems(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        if type(to_operate2) is Circl:
            new = []
            for elem in to_operate1.whole_list():
                new.append(Circl([str(float(i) - float(elem)) for i in to_operate2.whole_list()]))
            main_circl.append(Circl(new))
        else:
            main_circl.append(Circl([str(float(to_operate2) - float(i)) for i in to_operate1.whole_list()]))
    else:
        if type(to_operate2) is Circl:
            main_circl.append(Circl([str(float(to_operate1) - float(i)) for i in to_operate2.whole_list()]))
        else:
            main_circl.append(str(float(to_operate1) - float(to_operate2)))

def c_mul_circl_elems(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        if type(to_operate2) is Circl:
            new = []
            for elem in to_operate1.whole_list():
                new.append(Circl([str(float(i) * float(elem)) for i in to_operate2.whole_list()]))
            main_circl.append(Circl(new))
        else:
            main_circl.append(Circl([str(float(to_operate2) * float(i)) for i in to_operate1.whole_list()]))
    else:
        if type(to_operate2) is Circl:
            main_circl.append(Circl([str(float(to_operate1) * float(i)) for i in to_operate2.whole_list()]))
        else:
            main_circl.append(str(float(to_operate1) * float(to_operate2)))

def c_div_circl_elems(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        if type(to_operate2) is Circl:
            new = []
            for elem in to_operate1.whole_list():
                new.append(Circl([str(float(i) / float(elem)) for i in to_operate2.whole_list()]))
            main_circl.append(Circl(new))
        else:
            main_circl.append(Circl([str(float(to_operate2) / float(i)) for i in to_operate1.whole_list()]))
    else:
        if type(to_operate2) is Circl:
            main_circl.append(Circl([str(float(to_operate1) / float(i)) for i in to_operate2.whole_list()]))
        else:
            main_circl.append(str(float(to_operate1) / float(to_operate2)))


def c_mod_circl_elems(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        to_operate2 = main_circl.pop()
        if type(to_operate2) is Circl:
            new = []
            for elem in to_operate1.whole_list():
                new.append(Circl([str(float(i) % float(elem)) for i in to_operate2.whole_list()]))
            main_circl.append(Circl(new))
        else:
            main_circl.append(Circl([str(float(to_operate2) % float(i)) for i in to_operate1.whole_list()]))
    else:
        to_operate2 = main_circl.pop()
        if type(to_operate2) is Circl:
            main_circl.append(Circl([str(float(to_operate1) % float(i)) for i in to_operate2.whole_list()]))
        else:
            main_circl.append(str(float(to_operate1) % float(to_operate2)))


def c_negate(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(Circl([str(-float(i)) for i in to_operate1.whole_list()]))
    else:
        main_circl.append(str(-float(to_operate1)))


def c_merge(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl and type(to_operate2) is Circl:
        main_circl.append(Circl(to_operate2.whole_list() + to_operate1.whole_list()))
    elif type(to_operate1) is Circl:
        main_circl.append(Circl([to_operate2] + to_operate1.whole_list()))
    elif type(to_operate2) is Circl:
        main_circl.append(Circl(to_operate2.whole_list() + [to_operate1]))
    else:
        main_circl.append(to_operate2 + to_operate1)


def c_mul_circlify(main_circl: Circl, main_program: Program):
    to_operate1 = int(float(main_circl.pop()))
    to_operate2 = main_circl.pop()
    main_circl.append(Circl([to_operate2] * to_operate1))


def c_typeof(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    main_circl.append(to_operate1)
    main_circl.append("circl" if type(to_operate1) is Circl else "string")


def c_unknown_instruction6(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    if type(to_operate1) is Circl:
        seen = []
        result = []
        for i in to_operate1.whole_list():
            if i not in seen:
                seen.append(i)
                result.append(i)
        main_circl.append(Circl(result))
    else:
        seen = []
        result = []
        for i in to_operate1:
            if i not in seen:
                seen.append(i)
                result.append(i)
        main_circl.append("".join(result))


def c_unknown_instruction7(main_circl: Circl, main_program: Program):
    to_operate1 = int(float(main_circl.pop()))
    items = []
    for i in range(to_operate1):
        items.append(main_circl.pop())
    main_circl.append(Circl(list(reversed(items))))


def c_append_program_counter(main_circl: Circl, main_program: Program):
    main_circl.append(str(main_program.counter))


def c_count(main_circl: Circl, main_program: Program):
    to_operate1 = main_circl.pop()
    to_operate2 = main_circl.pop()
    if type(to_operate1) is Circl:
        main_circl.append(str(to_operate1.whole_list().count(to_operate2)))
    else:
        main_circl.append(str(to_operate1.count(to_operate2)))

# MAIN INSTRUCTION SET
# Each declared function above should correspond to a character (i.e. command)
instruction_set: Dict[str, Callable[[Circl, Program], None]] = {
    ".": c_halt,
    "˅": c_read_input,
    "π": c_pi,
    "ε": c_e,
    "∞": c_inf,
    "⧺": c_duplicate,
    "↓": c_pop,
    "⟲": c_cycle_back,
    "⟳": c_cycle_forward,
    "⇄": c_swap_last,
    "@": c_move_top,
    "^": c_println,
    "§": c_print,
    "←": c_read_file,
    "→": c_write_file,
    "⇀": c_length,
    "⦰": c_radius,
    "♯": c_cast_float,
    "♭": c_cast_int,
    "Φ": c_to_precision,
    "Ψ": c_ordinal,
    "Ω": c_cast_char,
    "⚂": c_rnd,
    "¬": c_logical_not,
    "∧": c_conjoin,
    "∨": c_disjoin,
    "⊕": c_logical_xor,
    "⋘": c_left_shift,
    "⋙": c_right_shift,
    "=": c_equals,
    "≠": c_not_equals,
    "<": c_lower_than,
    ">": c_greater_than,
    "≤": c_lower_than_equal,
    "≥": c_greater_than_equal,
    "⁇": c_truthy_program_counter_increment,
    "‽": c_falsy_program_counter_increment,
    "⇒": c_increment_program_counter_by,
    "⇐": c_decrement_program_counter_by,
    "↺": c_execute_as_circl,
    "⊲": c_remove_nth_element,
    "⊳": c_remove_negative_nth_element,
    "⊙": c_set_index_zero,
    "⡳": c_append_range,
    "⇡": c_append_range_circl,
    "²": c_square,
    "√": c_sqrt,
    "ⁿ": c_pow,
    "⌊": c_floor,
    "⌈": c_ceil,
    "○": c_round,
    "⌃": c_max,
    "⌄": c_min,
    "|": c_abs,
    "ℓ": c_logn,
    "ℒ": c_log10,
    "∿": c_sin,
    "⌒": c_cos,
    "∡": c_tan,
    "✄": c_split,
    "⊂": c_inclusion,
    "↔": c_unknown1,
    "⬆": c_uppercase,
    "⬇": c_lowercase,
    "∑": c_sum,
    "⊗": c_mul,
    "∈": c_contains,
    "∉": c_not_contains,
    "⍳": c_indexof,
    "∩": c_join,
    "∪": c_union,
    "⊖": c_disjunctive_union,
    "⊛": c_unknown_instruction1,
    "Δ": c_unknown_instruction2,
    "⌀": c_this_length,
    "κ": c_unknown_instruction3,
    "ρ": c_reverse,
    "χ": c_unknown_instruction4,
    "≡": c_equivalent,
    "‾": c_circlify,
    "_": c_add_all,
    "⋃": c_unknown_instruction5,
    "✂": c_split_circlify,
    "+": c_add_circl_elems,
    "-": c_sub_circl_elems,
    "×": c_mul_circl_elems,
    "÷": c_div_circl_elems,
    "%": c_mod_circl_elems,
    "⁻": c_negate,
    "∥": c_merge,
    "⊡": c_mul_circlify,
    "τ": c_typeof,
    "⌂": c_unknown_instruction6,
    "⊤": c_unknown_instruction7,
    "⊞": c_append_program_counter,
    "ν": c_count
}