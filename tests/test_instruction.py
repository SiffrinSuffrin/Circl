import unittest

from src.circl.instruction_set import *


# TODO: c_read_input
# TODO: c_duplicate
# TODO: c_pop
# TODO: c_cycle_back
# TODO: c_cycle_forward
# TODO: c_swap_last
# TODO: c_move_top
# TODO: c_println
# TODO: c_print
# TODO: c_read_file
# TODO: c_write_file
# TODO: c_length
# TODO: c_radius
# TODO: c_cast_float
# TODO: c_cast_int
# TODO: c_to_precision
# TODO: c_ordinal
# TODO: c_cast_char
# TODO: c_rnd
# TODO: c_equals
# TODO: c_not_equals
# TODO: c_lower_than
# TODO: c_greater_than
# TODO: c_lower_than_equal
# TODO: c_greater_than_equal
# TODO: c_jump_if_true
# TODO: c_jump_if_false
# TODO: c_increment_program_counter_by
# TODO: c_decrement_program_counter_by
# TODO: c_execute_as_circl
# TODO: c_remove_nth_element
# TODO: c_remove_negative_nth_element
# TODO: c_set_index_zero
# TODO: c_append_range
# TODO: c_append_range_circl
# TODO: c_square
# TODO: c_sqrt
# TODO: c_floor
# TODO: c_ceil
# TODO: c_round
# TODO: c_max
# TODO: c_min
# TODO: c_abs
# TODO: c_logn
# TODO: c_log10
# TODO: c_sin
# TODO: c_cos
# TODO: c_tan
# TODO: c_split
# TODO: c_slice
# TODO: c_replace_string
# TODO: c_uppercase
# TODO: c_lowercase
# TODO: c_sum
# TODO: c_product
# TODO: c_contains
# TODO: c_not_contains
# TODO: c_indexof
# TODO: c_intersection
# TODO: c_stack_size
# TODO: c_sort
# TODO: c_reverse
# TODO: c_replace
# TODO: c_all_elements_equal
# TODO: c_circlify
# TODO: c_uncirclify
# TODO: c_str_join
# TODO: c_str_split
# TODO: c_negate
# TODO: c_mul_circlify
# TODO: c_typeof
# TODO: c_unique
# TODO: c_circlify_multiple
# TODO: c_append_program_counter
# TODO: c_count
# TODO: c_regex_match


class TestInstructionSet(unittest.TestCase):
    def setUp(self):
        self.emptyCircl = Circl()

    def test_c_halt(self):
        test_cases = [None,[], ["foo","bar"], [1,2,3], [Circl(["foo"]),Circl(["bar"])]]
        for test_case in test_cases:
            circl = Circl(test_case)
            c_halt(circl)
            self.assertEqual(circl,self.emptyCircl)

    def test_c_logical_not(self):
        test_cases = [(Circl([2,1,0]), Circl([2,1,True])),
                      (Circl([Circl([5, 0, Circl([1,2,3]), Circl([])])]), Circl([Circl([False,True,False,True])])),
                      (Circl([Circl(["", "0", "4", ""])]), Circl([Circl([True, False, False, True])])),
                      (Circl([Circl([])]), Circl([Circl([])])),
                      (Circl([True]), Circl([False])),
                      (Circl([False]), Circl([True])),
                      ]

        for test, result in test_cases:
            c_logical_not(test)
            self.assertEqual(test, result)

    def test_c_logical_and(self):
        test_cases = [(Circl([2, 1, 0]), Circl([2, False])),
                      (Circl([1, Circl([1, 0, 1, 0])]), Circl([Circl([True, False, True, False])])),
                      (Circl([Circl([1, 1, 0, 0]), 1]), Circl([Circl([True, True, False, False])])),
                      (Circl([Circl([1, 1, 0, 0]), Circl([1, 0, 1, 0])]), Circl([Circl([True, False, False, False])])),
                      ]

        for test, result in test_cases:
            c_logical_and(test)
            self.assertEqual(test, result)

    def test_c_logical_or(self):
        test_cases = [(Circl([2, 1, 0]), Circl([2, True])),
                      (Circl([0, Circl([1, 0, 1, 0])]), Circl([Circl([True, False, True, False])])),
                      (Circl([Circl([1, 1, 0, 0]), 0]), Circl([Circl([True, True, False, False])])),
                      (Circl([Circl([1, 1, 0, 0]), Circl([1, 0, 1, 0])]), Circl([Circl([True, True, True, False])])),
                      ]

        for test, result in test_cases:
            c_logical_or(test)
            self.assertEqual(test, result)

    def test_c_logical_xor(self):
        test_cases = [(Circl([2, 1, 0]), Circl([2, True])),
                      (Circl([1, Circl([1, 0, 1, 0])]), Circl([Circl([False, True, False, True])])),
                      (Circl([Circl([1, 1, 0, 0]), 0]), Circl([Circl([True, True, False, False])])),
                      (Circl([Circl([1, 1, 0, 0]), Circl([1, 0, 1, 0])]), Circl([Circl([False, True, True, False])])),
                      ]

        for test, result in test_cases:
            c_logical_xor(test)
            self.assertEqual(test, result)

    def test_c_left_shift(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, 7 << 8])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([1 << 5, 1 << 6, 1 << 7, 1 << 8])])),
                      (Circl([Circl([1, 2, 3, 4]), 2]), Circl([Circl([1 << 2, 2 << 2, 3 << 2, 4 << 2])])),
                      (Circl([Circl([10, 200, 3000, 4000]), Circl([1, 2, 3, 4])]),
                       Circl([Circl([10 << 1, 200 << 2, 3000 << 3, 4000 << 4])])),
                      ]

        for test, result in test_cases:
            c_left_shift(test)
            self.assertEqual(test, result)

    def test_c_right_shift(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, 7 >> 8])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([1 >> 5, 1 >> 6, 1 >> 7, 1 >> 8])])),
                      (Circl([Circl([1, 2, 3, 4]), 2]), Circl([Circl([1 >> 2, 2 >> 2, 3 >> 2, 4 >> 2])])),
                      (Circl([Circl([10, 200, 3000, 4000]), Circl([1, 2, 3, 4])]),
                       Circl([Circl([10 >> 1, 200 >> 2, 3000 >> 3, 4000 >> 4])])),
                      ]

        for test, result in test_cases:
            c_right_shift(test)
            self.assertEqual(test, result)

    def test_c_pow(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, 7 ** 8])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([1, 1, 1, 1])])),
                      (Circl([Circl([1, 2, 3, 4]), 2]), Circl([Circl([1, 4, 9, 16])])),
                      (Circl([Circl([1, 2, 3, 4]), Circl([1, 2, 3, 4])]), Circl([Circl([1, 4, 27, 256])])),
                      ]

        for test, result in test_cases:
            c_pow(test)
            self.assertEqual(test, result)

    def test_c_union(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, Circl([7, 8])])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([1, 5, 6, 7, 8])])),
                      (Circl([Circl([1, 2, 3, 4]), 5]), Circl([Circl([1, 2, 3, 4, 5])])),
                      (Circl([Circl([1, 2, 3, Circl([4])]), Circl([5, 6, 7, Circl([8])])]),
                       Circl([Circl([1, 2, 3, Circl([4]), 5, 6, 7, Circl([8])])])),
                      ]

        for test, result in test_cases:
            c_union(test)
            self.assertEqual(self.freeze_circle(test), self.freeze_circle(result))

    def freeze_circle(self, circl_or_point: Circl | Point):
        return frozenset(map(lambda x: self.freeze_circle(x), circl_or_point)) if isinstance(circl_or_point,
                                                                                             Circl) else circl_or_point

    def test_c_zip(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, Circl([7, 8])])),
                      (Circl([1, Circl([5, 6, 7, 8])]),
                       Circl([Circl([Circl([1, 5]), Circl([1, 6]), Circl([1, 7]), Circl([1, 8])])])),
                      (Circl([Circl([1, 2, 3, 4]), 5]),
                       Circl([Circl([Circl([1, 5]), Circl([2, 5]), Circl([3, 5]), Circl([4, 5])])])),
                      (Circl([Circl([1, 2, 3, 4]), Circl([5, 6, 7, 8])]),
                       Circl([Circl([Circl([1, 5]), Circl([2, 6]), Circl([3, 7]), Circl([4, 8])])])),
                      ]

        for test, result in test_cases:
            c_zip(test)
            self.assertEqual(test, result)

    def test_c_add_circl_elems(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, 15])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([6, 7, 8, 9])])),
                      (Circl([Circl([1, 2, 3, 4]), 5]), Circl([Circl([6, 7, 8, 9])])),
                      (Circl([Circl([1, 2, 3, 4]), Circl([5, 6, 7, 8])]), Circl([Circl([6, 8, 10, 12])])),
                      ]

        for test, result in test_cases:
            c_add_circl_elems(test)
            self.assertEqual(test, result)

    def test_c_sub_circl_elems(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, -1])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([-4, -5, -6, -7])])),
                      (Circl([Circl([1, 2, 3, 4]), 5]), Circl([Circl([-4, -3, -2, -1])])),
                      (Circl([Circl([1, 2, 3, 4]), Circl([5, 6, 7, 8])]), Circl([Circl([-4, -4, -4, -4])])),
                      ]

        for test, result in test_cases:
            c_sub_circl_elems(test)
            self.assertEqual(test, result)

    def test_c_mul_circl_elems(self):
        test_cases = [(Circl([5, 6, 7, 8]), Circl([5, 6, 56])),
                      (Circl([1, Circl([5, 6, 7, 8])]), Circl([Circl([5, 6, 7, 8])])),
                      (Circl([Circl([1, 2, 3, 4]), 5]), Circl([Circl([5, 10, 15, 20])])),
                      (Circl([Circl([1, 2, 3, 4]), Circl([5, 6, 7, 8])]), Circl([Circl([5, 12, 21, 32])])),
                      ]

        for test, result in test_cases:
            c_mul_circl_elems(test)
            self.assertEqual(test, result)

    def test_c_div_circl_elems(self):
        test_cases = [(Circl([5, 6, 16, 8]), Circl([5, 6, 2])),
                      (Circl([420, Circl([5, 6, 7, 8])]), Circl([Circl([84, 70, 60, 52.5])])),
                      (Circl([Circl([10, 20, 30, 40]), 5]), Circl([Circl([2, 4, 6, 8])])),
                      (Circl([Circl([420, 840, 1260, 80]), Circl([5, 6, 7, 8])]), Circl([Circl([84, 140, 180, 10])])),
                      ]

        for test, result in test_cases:
            c_div_circl_elems(test)
            self.assertEqual(test, result)

    def test_c_mod_circl_elems(self):
        test_cases = [(Circl([5, 6, 16, 8]), Circl([5, 6, 0])),
                      (Circl([123, Circl([5, 6, 7, 9])]), Circl([Circl([3, 3, 4, 6])])),
                      (Circl([Circl([11, 22, 33, 44]), 5]), Circl([Circl([1, 2, 3, 4])])),
                      (Circl([Circl([10, 20, 29, 43]), Circl([2, 3, 4, 5])]), Circl([Circl([0, 2, 1, 3])])),
                      ]

        for test, result in test_cases:
            c_mod_circl_elems(test)
            self.assertEqual(test, result)

    def test_c_extend(self):
        test_cases = [(Circl([5, 6, 16, 8]), Circl([5, 6, Circl([16, 8])])),
                      (Circl([123, Circl([5, "6", 7, 9])]), Circl([Circl([123, 5, "6", 7, 9])])),
                      (Circl([Circl([11, "22", 33, "44"]), "5"]), Circl([Circl([11, "22", 33, "44", "5"])])),
                      (Circl([Circl([10, 20, 29, 43]), Circl([2, 3, 4, 5])]),
                       Circl([Circl([10, 20, 29, 43, 2, 3, 4, 5])])),
                      (Circl(["abc", "def"]), Circl(["abcdef"])),
                      (Circl(["abc", 456]), Circl([Circl(["abc", 456])])),
                      (Circl([123, "def"]), Circl([Circl([123, "def"])])),
                      ]

        for test, result in test_cases:
            c_extend(test)
            self.assertEqual(test, result)

    def test_c_var_push(self):
        # TODO after the var_circl gets rewritten
        pass

    def test_c_var_pull(self):
        # TODO after the var_circl gets rewritten
        pass

    def test_c_var_del(self):
        # TODO after the var_circl gets rewritten
        pass


if __name__ == '__main__':
    unittest.main()