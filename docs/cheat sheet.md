# Cheat sheet for Circl

Hi. First version here. Probably needs some work, revisions and additions.

# Syntax

# Semantics

## Special Values

| Operator | Function   | Semantic |
|----------|------------|----------|
|  π       | c_pi       | 3.14     |
|  ε       | c_e        | 2.71     |
|  ∞       | c_infinity | infinity |

## Operators
TODO: sort operators into groups like arithmetic, sets, logical, etc. for better readability 

| Operator | Function                       | Semantic                                                                                                                                                                    |
|----------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .        | c_halt                         | halt instruction                                                                                                                                                            |
| ˅        | c_read_input                   | console input                                                                                                                                                               |
| ⧺        | c_duplicate                    | double instruction                                                                                                                                                          |
| ↓        | c_pop                          | pop instruction                                                                                                                                                             |
| ↶        | c_cycle_back                   | rotate (3 2 1) into (2 1 3)                                                                                                                                                 |
| ↷        | c_cycle_forward                | rotate (3 2 1) into (1 3 2)                                                                                                                                                 |
| ⇄        | c_swap_last                    | swap (2 1) to (1 2)                                                                                                                                                         |
| @        | c_move_top                     | takes n-th instruction and puts it on top?                                                                                                                                  |
| ^        | c_println                      | println symbol                                                                                                                                                              |
| §        | c_print                        | print symbol                                                                                                                                                                |
| ←        | c_read_file                    | read file                                                                                                                                                                   |
| →        | c_write_file                   | write file. first argument is name. second is contents                                                                                                                      |
| ⇀        | c_length                       | turn str/circl into length                                                                                                                                                  |
| ⦰        | c_radius                       | get radius                                                                                                                                                                  |
| ♯        | c_cast_float                   | type cast number or number-circl to float                                                                                                                                   |
| ♭        | c_cast_int                     | type cast number or number-circl to int                                                                                                                                     |
| Φ        | c_to_precision                 | format 1st number or number-circl to precision of 2nd argument                                                                                                              |
| Ψ        | c_ordinal                      | turn argument into ord() of argument                                                                                                                                        |
| Ω        | c_cast_char                    | turn argument into char based on unicode ordinals                                                                                                                           |
| ⚂        | c_rnd                          | if operator is a circl it selects a random element from it. <br/> is the operator is 1 it makes a random number between [0,1) <br/> otherwise between 0 and the operator    |
| ¬        | c_logical_not                  | 1 if operator is falsy otherwise 0. <br/> Or does that for every element in the circle                                                                                      |
| ∧        | c_logical_and                  | zips 2 circles using logical and as operator<br/>or does logical and between an operator and every part of a circle<br/>or logical and between 2 operators                  |
| ∨        | c_logical_or                   | zips 2 circles using logical or as operator<br/>or does logical or between an operator and every part of a circle<br/>or logical and between 2 operators                    |
| ⊕        | c_logical_xor                  | bitwise xor between the contents of 2 zipped circls <br/>or 1 operator and the contents of another circles<br/>or 2 operators                                               |
| ⋘        | c_left_shift                   | left shifts first operators contents by 2nd operators contents. zips circles, does elementwise operation with circl and operator, or just normal bitshift with 2 operators  |
| ⋙        | c_right_shift                  | right shifts first operators contents by 2nd operators contents. zips circles, does elementwise operation with circl and operator, or just normal bitshift with 2 operators |
| =        | c_equals                       | checks equality between 2 circles or 2 operators. "1" if equal. "0" if not                                                                                                  |
| ≠        | c_not_equals                   | checks inequality between 2 circles or 2 operators. "1" if unequal. "0" if not                                                                                              |
| <        | c_lower_than                   | compares 2 numbers. No circles for now?                                                                                                                                     |
| \>       | c_greater_than                 | compares 2 numbers. No circles for now?                                                                                                                                     |
| ≤        | c_lower_than_equal             | compares 2 numbers. No circles for now?                                                                                                                                     |
| ≥        | c_greater_than_equal           | compares 2 numbers. No circles for now?                                                                                                                                     |
| ⁇        | c_jump_if_true                 | takes 2 operators. If 1st operator is truthy sets program counter to 2nd operator                                                                                           |
| ‽        | c_jump_if_false                | takes 2 operators. If 1st operator is falsy sets program counter to 2nd operator                                                                                            |
| ⇒        | c_increment_program_counter_by | adds an integer to the program counter                                                                                                                                      |
| ⇐        | c_decrement_program_counter_by | subtracts an integer from the program counter                                                                                                                               |
| ↺        | c_execute_as_circl             | executes operator as circle. Be aware of possible infinite loops                                                                                                            |
| ⊲        | c_remove_nth_element           | uses a number n to delete the n-th element of the 2nd argument.                                                                                                             |
| ⊳        | c_remove_negative_nth_element  | uses a number n to delete the -n-th element of the 2nd argument.                                                                                                            |
| ⊙        | c_set_index_zero               | rotates the circle around such that the argument n becomes the new index 0                                                                                                  |
| ⡳        | c_append_range                 | makes a range from 0 to number or from the first argument of a circl to the 2nd one                                                                                         |
| ⇡        | c_append_range_circl           | appends range from 0 to number. In the case of circl it appends a circl containing ranges from 0 to n for every n in the circl                                              |
| ²        | c_square                       | squares a number or all numbers in a circl                                                                                                                                  |
| √        | c_sqrt                         | applies squareroot to a number or all numbers in a circl                                                                                                                    |
| ⁿ        | c_pow                          | takes to arguments. raises the 2nd to the power of the first                                                                                                                |
| ⌊        | c_floor                        | rounds down a number or all numbers in a circl                                                                                                                              |
| ⌈        | c_ceil                         | rounds up a number or all numbers in a circl                                                                                                                                |
| ○        | c_round                        | rounds a number or all numbers in a circl                                                                                                                                   |
| ⌃        | c_max                          | max()                                                                                                                                                                       |
| ⌄        | c_min                          | min()                                                                                                                                                                       |
| \|       | c_abs                          | abs()                                                                                                                                                                       |
| ℓ        | c_logn                         | math.log()                                                                                                                                                                  |
| ℒ        | c_log10                        | math.log10()                                                                                                                                                                |
| ∿        | c_sin                          | math.sin()                                                                                                                                                                  |
| ⌒        | c_cos                          | math.cos()                                                                                                                                                                  |
| ∡        | c_tan                          | math.tan()                                                                                                                                                                  |
| ✄        | c_split                        | cuts up an argument into a list of its elements. Or cuts up every element of a circle                                                                                       |
| ⊂        | c_slice                        | takes 3 operators. A list. A stop. A start. And adds `list[start:stop]` to the stack                                                                                        |
| ↔        | c_replace_string               | takes 3 operators. str or circl. replacing string, replaced string. See str.replace(). <br/> If 1st operator is a circl calls replace() on all strings it contains          |
| ⬆        | c_uppercase                    | calls str.upper() on string or all strings in a circl                                                                                                                       |
| ⬇        | c_lowercase                    | calls str.lower() on string or all strings in a circl                                                                                                                       |
| ∑        | c_sum                          | takes 1 operator. applies sum() on a circl or just appends operator again if not a circl                                                                                    |
| Π        | c_product                      | takes 1 operator. applies sum() on a circl or just appends operator again if not a circl                                                                                    |
| ∈        | c_contains                     | checks if operator 2 is an element of operator 1                                                                                                                            |
| ∉        | c_not_contains                 | checks if operator 2 is not an element of operator 1                                                                                                                        |
| ⍳        | c_indexof                      | searches for operator 2 in operator 1 and returns the lowest index where it was found.                                                                                      |
| ∩        | c_intersection                 | Does an intersection between 2 operators. Adds only values that are in both operators                                                                                       |
| ∪        | c_union                        | Does a union of 2 operators. Adds values that are in either operator                                                                                                        |
| ⊖        | c_difference                   | Does a set theory difference. operator 2\\operator 1.Adds all values that are only in operator2  <br/>TODO: consider flipping?                                              |
| ⊛        | c_zip                          | Zips together 2 circls. Or zips a circl with an `list(operator)`                                                                                                            |
| ⌀        | c_stack_size                   | Appends the size of the main_circl to the stack                                                                                                                             |
| κ        | c_sort                         | Sorts a number circl using a very weird lambda. <br/>TODO: check if this can be improved                                                                                    |
| ρ        | c_reverse                      | Reverses a circl or str                                                                                                                                                     |
| χ        | c_replace                      | Replaces the operator2-th index of operator1 with operator3                                                                                                                 |
| ≡        | c_all_elements_equal           | Checks if all elements of a circl or str are the same                                                                                                                       |
| ‾        | c_circlify                     | Wraps an argument in a circl                                                                                                                                                |
| _        | c_uncirclify                   | Unwraps a circl and puts its contents on the stack<br/> TODO str? int?                                                                                                      |
| ⋃        | c_str_join                     | Joins all contents of operator1 with every element of operator2 as separators. see str.join()<br/>TODO: might use a refactor?                                               |
| ✂        | c_str_split                    | see str.split. Basically opposite of str.join        <br/>TODO: might also use a refactor?                                                                                  |
| +        | c_add_circl_elems              | Adds 2 arguments elementwise                                                                                                                                                |
| -        | c_sub_circl_elems              | Subtracts 2 arguments elementwise. Operator2 - Operator1                                                                                                                    |
| ×        | c_mul_circl_elems              | Multiplies 2 arguments elementwise                                                                                                                                          |
| ÷        | c_div_circl_elems              | Divides 2 arguments elementwise. Operator2 / Operator1                                                                                                                      |
| %        | c_mod_circl_elems              | Takes the modulus elementwise. Operator2 % Operator1                                                                                                                        |
| ⁻        | c_negate                       | flips the sign of every element of a circl or of a number                                                                                                                   |
| ∥        | c_extend                       | Appends two operators into a single circl. Except for 2 strings which get concatenated.                                                                                     |
| ⊡        | c_mul_circlify                 | Does []*n which repeats the list n times. operator 1 is the n and operator 2 is the circle                                                                                  |
| τ        | c_typeof                       | Appends the type of an operator on the stack                                                                                                                                |
| ⌂        | c_unique                       | Removes duplicates from a circl or str                                                                                                                                      |
| ⊤        | c_circlify_multiple            | Takes 1 number as argument. Pops that many items of the stack and puts them in a circle<br/>TODO: kinda a duplicate of c_circlify                                           |
| ⊞        | c_append_program_counter       | Appends the current program counter                                                                                                                                         |
| ν        | c_count                        | Counts the number of occurences of operator2 in operator1                                                                                                                   |
| ↦        | c_var_push                     | takes arguments b a, uses a as a variable id and stores the contents of b in the variable circle                                                                            |
| ↤        | c_var_pull                     | takes argument a and uses it as a variable id to retrieve it from the variable circle                                                                                       |
| 🜏       | c_var_del                      | takes argument and uses it as an id to delete a variable that is saved under it                                                                                             |
| Я        | c_regex_match                  | takes 2 off the top of the stack, performs re.findall (if either operand is a circl, applies the operation for each) and returns the results on a circl <br/>               |
