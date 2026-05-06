# Cheat sheet for Circl

Hi. First version here. Probably needs some work, revisions and additions.

# Syntax

# Semantics

## Special Values

| Operator | Name     | Semantic |
|----------|----------|----------|
|  π       | pi       | 3.14     |
|  ε       | e        | 2.71     |
|  ∞       | infinity | infinity |

## Operators
TODO: sort operators into groups like arithmetic, sets, logical, etc. for better readability 

| Operator | Name                   | Semantic                                                                                                                                                                    |
|----------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .        | dot                    | halt instruction                                                                                                                                                            |
| ˅        |                        | console input                                                                                                                                                               |
| ⧺        |                        | double instruction                                                                                                                                                          |
| ↓        | down arrow             | pop instruction                                                                                                                                                             |
| ⟲        | ccw rotate             | rotate (3 2 1) into (2 1 3)                                                                                                                                                 |
| ⟳        | cw rotate              | rotate (3 2 1) into (1 3 2)                                                                                                                                                 |
| ⇄        |                        | swap (2 1) to (1 2)                                                                                                                                                         |
| @        | at                     | takes n-th instruction and puts it on top?                                                                                                                                  |
| ^        | caret                  | println symbol                                                                                                                                                              |
| §        | paragraph              | print symbol                                                                                                                                                                |
| ←        | left arrow             | read file                                                                                                                                                                   |
| →        | right arrow            | write file. first argument is name. second is contents                                                                                                                      |
| ⇀        | rightwards harpoon     | turn str/circl into length                                                                                                                                                  |
| ⦰        | Empty set              | get radius                                                                                                                                                                  |
| ♯        | sharp                  | type cast number or number-circl to float                                                                                                                                   |
| ♭        | flat                   | type cast number or number-circl to int                                                                                                                                     |
| Φ        | phi                    | format 1st number or number-circl to precision of 2nd argument                                                                                                              |
| Ψ        | psi                    | turn argument into ord() of argument                                                                                                                                        |
| Ω        | omega                  | turn argument into char based on unicode ordinals                                                                                                                           |
| ⚂        | dice                   | if operator is a circl it selects a random element from it. <br/> is the operator is 1 it makes a random number between [0,1) <br/> otherwise between 0 and the operator    |
| ¬        | not                    | 1 if operator is falsy otherwise 0. <br/> Or does that for every element in the circle                                                                                      |
| ∧        | conjunction            | zips 2 circles using logical and as operator<br/>or does logical and between an operator and every part of a circle<br/>or logical and between 2 operators                  |
| ∨        | disjunction            | zips 2 circles using logical or as operator<br/>or does logical or between an operator and every part of a circle<br/>or logical and between 2 operators                    |
| ⊕        | circled plus           | bitwise xor between the contents of 2 zipped circls <br/>or 1 operator and the contents of another circles<br/>or 2 operators                                               |
| ⋘        | very much less then    | left shifts first operators contents by 2nd operators contents. zips circles, does elementwise operation with circl and operator, or just normal bitshift with 2 operators  |
| ⋙        | very much greater then | right shifts first operators contents by 2nd operators contents. zips circles, does elementwise operation with circl and operator, or just normal bitshift with 2 operators |
| =        | equal                  | checks equality between 2 circles or 2 operators. "1" if equal. "0" if not                                                                                                  |
| ≠        | not equal              | checks inequality between 2 circles or 2 operators. "1" if unequal. "0" if not                                                                                              |
| <        | less than              | compares 2 numbers. No circles for now?                                                                                                                                     |
| \>       | greater than           | compares 2 numbers. No circles for now?                                                                                                                                     |
| ≤        | less than or equal     | compares 2 numbers. No circles for now?                                                                                                                                     |
| ≥        | greater than or equal  | compares 2 numbers. No circles for now?                                                                                                                                     |
| ⁇        |                        | takes 2 operators. adds integer value of 1st operator to program counter                                                                                                    |
| ‽        |                        | takes 2 operators. adds integer value of 2st operator to program counter                                                                                                    |
| ⇒        | double right arrow     | adds an integer to the program counter                                                                                                                                      |
| ⇐        | double left arrow      | sets program counter to integer                                                                                                                                             |
| ↺        | ccw open circle arrow  | executes operator as circle. Be aware of possible infinite loops                                                                                                            |
| ⊲        |                        | uses a number n to delete the n-th element of the 2nd argument.                                                                                                             |
| ⊳        |                        | uses a number n to delete the -n-th element of the 2nd argument.                                                                                                            |
| ⊙        | circled dot            | rotates the circle around such that the argument n becomes the new index 0                                                                                                  |
| ⡳        | some braile letter idk | makes a range from 0 to number or from the first argument of a circl to the 2nd one                                                                                         |
| ⇡        | dotted up arrow        | appends range from 0 to number. In the case of circl it appends a circl containing ranges from 0 to n for every n in the circl                                              |
| ²        | squared                | squares a number or all numbers in a circl                                                                                                                                  |
| √        | square root            | applies squareroot to a number or all numbers in a circl                                                                                                                    |
| ⁿ        |                        | takes to arguments. raises the 2nd to the power of the first                                                                                                                |
| ⌊        | floor                  | rounds down a number or all numbers in a circl                                                                                                                              |
| ⌈        | ceiling                | rounds up a number or all numbers in a circl                                                                                                                                |
| ○        |                        | rounds a number or all numbers in a circl                                                                                                                                   |
| ⌃        |                        | max()                                                                                                                                                                       |
| ⌄        |                        | min()                                                                                                                                                                       |
| \|       |                        | abs()                                                                                                                                                                       |
| ℓ        |                        | math.log()                                                                                                                                                                  |
| ℒ        |                        | math.log10()                                                                                                                                                                |
| ∿        |                        | math.sin()                                                                                                                                                                  |
| ⌒        |                        | math.cos()                                                                                                                                                                  |
| ∡        |                        | math.tan()                                                                                                                                                                  |
| ✄        |                        | cuts up an argument into a list of its elements. Or cuts up every element of a circle                                                                                       |
| ⊂        |                        |                                                                                                                                                                             |
| ↔        |                        |                                                                                                                                                                             |
| ⬆        |                        |                                                                                                                                                                             |
| ⬇        |                        |                                                                                                                                                                             |
| ∑        | sigma                  |                                                                                                                                                                             |
| ⊗        |                        |                                                                                                                                                                             |
| ∈        |                        |                                                                                                                                                                             |
| ∉        |                        |                                                                                                                                                                             |
| ⍳        |                        |                                                                                                                                                                             |
| ∩        |                        |                                                                                                                                                                             |
| ∪        |                        |                                                                                                                                                                             |
| ⊖        |                        |                                                                                                                                                                             |
| ⊛        |                        |                                                                                                                                                                             |
| Δ        |                        |                                                                                                                                                                             |
| ⌀        |                        |                                                                                                                                                                             |
| κ        |                        |                                                                                                                                                                             |
| ρ        |                        |                                                                                                                                                                             |
| χ        |                        |                                                                                                                                                                             |
| ≡        |                        |                                                                                                                                                                             |
| ‾        |                        |                                                                                                                                                                             |
| _        |                        |                                                                                                                                                                             |
| ⋃        |                        |                                                                                                                                                                             |
| ✂        |                        |                                                                                                                                                                             |
| +        |                        |                                                                                                                                                                             |
| -        |                        |                                                                                                                                                                             |
| ×        |                        |                                                                                                                                                                             |
| ÷        |                        |                                                                                                                                                                             |
| %        |                        |                                                                                                                                                                             |
| ⁻        |                        |                                                                                                                                                                             |
| ∥        |                        |                                                                                                                                                                             |
| ⊡        |                        |                                                                                                                                                                             |
| τ        |                        |                                                                                                                                                                             |
| ⌂        |                        |                                                                                                                                                                             |
| ⊤        |                        |                                                                                                                                                                             |
| ⊞        |                        |                                                                                                                                                                             |
| ν        |                        |                                                                                                                                                                             |
