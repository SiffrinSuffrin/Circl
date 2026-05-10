import unittest

from src.circl.instruction_set import *
from src.circl.circl import Circl

# TODO: c_read_input
# TODO: c_pi
# TODO: c_e
# TODO: c_inf
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
# TODO: c_logical_not
# TODO: c_conjoin
# TODO: c_disjoin
# TODO: c_logical_xor
# TODO: c_left_shift
# TODO: c_right_shift
# TODO: c_equals
# TODO: c_not_equals
# TODO: c_lower_than
# TODO: c_greater_than
# TODO: c_lower_than_equal
# TODO: c_greater_than_equal
# TODO: c_truthy_program_counter_increment
# TODO: c_falsy_program_counter_increment
# TODO: c_increment_program_counter_by
# TODO: c_decrement_program_counter_by
# TODO: c_execute_as_circl, True
# TODO: c_remove_nth_element
# TODO: c_remove_negative_nth_element
# TODO: c_set_index_zero
# TODO: c_append_range
# TODO: c_append_range_circl
# TODO: c_square
# TODO: c_sqrt
# TODO: c_pow
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
# TODO: c_inclusion
# TODO: c_unknown1
# TODO: c_uppercase
# TODO: c_lowercase
# TODO: c_sum
# TODO: c_mul
# TODO: c_contains
# TODO: c_not_contains
# TODO: c_indexof
# TODO: c_join
# TODO: c_union
# TODO: c_disjunctive_union
# TODO: c_unknown_instruction1
# TODO: c_unknown_instruction2
# TODO: c_this_length
# TODO: c_unknown_instruction3
# TODO: c_reverse
# TODO: c_unknown_instruction4
# TODO: c_equivalent
# TODO: c_circlify
# TODO: c_add_all
# TODO: c_unknown_instruction5
# TODO: c_split_circlify
# TODO: c_add_circl_elems
# TODO: c_sub_circl_elems
# TODO: c_mul_circl_elems
# TODO: c_div_circl_elems
# TODO: c_mod_circl_elems
# TODO: c_negate
# TODO: c_merge
# TODO: c_mul_circlify
# TODO: c_typeof
# TODO: c_unknown_instruction6
# TODO: c_unknown_instruction7
# TODO: c_append_program_counter
# TODO: c_count


class TestInstructionSet(unittest.TestCase):
    def setUp(self):
        self.emptyCircl = Circl()

    def test_c_halt(self):
        test_cases = [None,[], ["foo","bar"], [1,2,3], [Circl(["foo"]),Circl(["bar"])]]
        for test_case in test_cases:
            circl = Circl()
            c_halt(circl)
            self.assertEqual(circl,self.emptyCircl)


if __name__ == '__main__':
    unittest.main()