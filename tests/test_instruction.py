import unittest

from src.circl.circl import Circl
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
# TODO: c_logical_not
# TODO: c_logical_and
# TODO: c_logical_or
# TODO: c_logical_xor
# TODO: c_left_shift
# TODO: c_right_shift
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
# TODO: c_union
# TODO: c_difference
# TODO: c_zip
# TODO: c_stack_size
# TODO: c_sort
# TODO: c_reverse
# TODO: c_replace
# TODO: c_all_elements_equal
# TODO: c_circlify
# TODO: c_uncirclify
# TODO: c_str_join
# TODO: c_str_split
# TODO: c_add_circl_elems
# TODO: c_sub_circl_elems
# TODO: c_mul_circl_elems
# TODO: c_div_circl_elems
# TODO: c_mod_circl_elems
# TODO: c_negate
# TODO: c_extend
# TODO: c_mul_circlify
# TODO: c_typeof
# TODO: c_unique
# TODO: c_circlify_multiple
# TODO: c_append_program_counter
# TODO: c_count
# TODO: c_var_push
# TODO: c_var_pull
# TODO: c_var_del
# TODO: c_regex_match


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