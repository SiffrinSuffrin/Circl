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

| Operator | Name               | Semantic                                                                                                                                                                 |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .        | dot                | noop                                                                                                                                                                     |
| ˅        |                    | console input                                                                                                                                                            |
| ⧺        |                    | double instruction                                                                                                                                                       |
| ↓        | down arrow         | pop instruction                                                                                                                                                          |
| ⟲        | ccw arrow          | rotate (3 2 1) into (2 1 3)                                                                                                                                              |
| ⟳        | cw arrow           | rotate (3 2 1) into (1 3 2)                                                                                                                                              |
| ⇄        |                    | swap (2 1) to (1 2)                                                                                                                                                      |
| @        | at                 | takes n-th instruction and puts it on top?                                                                                                                               |
| ^        | hat                | println symbol                                                                                                                                                           |
| §        | paragraph          | print symbol                                                                                                                                                             |
| ←        | left arrow         | read file                                                                                                                                                                |
| →        | right arrow        | write file. first argument is name. second is contents                                                                                                                   |
| ⇀        | rightwards harpoon | turn str/circl into length                                                                                                                                               |
| ⦰        | Empty set          | get radius                                                                                                                                                               |
| ♯        | sharp              | type cast number or number-circl to float                                                                                                                                |
| ♭        | flat               | type cast number or number-circl to int                                                                                                                                  |
| Φ        | phi                | format 1st number or number-circl to precision of 2nd argument                                                                                                           |
| Ψ        | psi                | turn argument into ord() of argument                                                                                                                                     |
| Ω        | omega              | turn argument into char based on unicode ordinals                                                                                                                        |
| ⚂        | dice               | if operator is a circl it selects a random element from it. <br/> is the operator is 1 it makes a random number between [0,1) <br/> otherwise between 0 and the operator |
| ¬        | not                | 1 if operator is falsy otherwise 0. <br/> Or does that for every element in the circle                                                                                   |
| ∧        | conjunction        |                                                                                                                                                                          |
| ∨        | disjunction        |                                                                                                                                                                          |
| ⊕        |                    |                                                                                                                                                                          |
| ⋘        |                    |                                                                                                                                                                          |
| ⋙        |                    |                                                                                                                                                                          |
| =        | equal              |                                                                                                                                                                          |
| ≠        | not equal          |                                                                                                                                                                          |
| <        |                    |                                                                                                                                                                          |
| \>       |                    |                                                                                                                                                                          |
| ≤        |                    |                                                                                                                                                                          |
| ≥        |                    |                                                                                                                                                                          |
| ⁇        |                    |                                                                                                                                                                          |
| ‽        |                    |                                                                                                                                                                          |
| ⇒        |                    |                                                                                                                                                                          |
| ⇐        |                    |                                                                                                                                                                          |
| ↺        |                    |                                                                                                                                                                          |
| ⊲        |                    |                                                                                                                                                                          |
| ⊳        |                    |                                                                                                                                                                          |
| ⊙        |                    |                                                                                                                                                                          |
| ⡳        |                    |                                                                                                                                                                          |
| ⇡        |                    |                                                                                                                                                                          |
| ²        | squared            |                                                                                                                                                                          |
| √        |                    |                                                                                                                                                                          |
| ⁿ        |                    |                                                                                                                                                                          |
| ⌊        |                    |                                                                                                                                                                          |
| ⌈        |                    |                                                                                                                                                                          |
| ○        |                    |                                                                                                                                                                          |
| ⌃        |                    |                                                                                                                                                                          |
| ⌄        |                    |                                                                                                                                                                          |
| \|       |                    |                                                                                                                                                                          |
| ℓ        |                    |                                                                                                                                                                          |
| ℒ        |                    |                                                                                                                                                                          |
| ∿        |                    |                                                                                                                                                                          |
| ⌒        |                    |                                                                                                                                                                          |
| ∡        |                    |                                                                                                                                                                          |
| ✄        |                    |                                                                                                                                                                          |
| ⊂        |                    |                                                                                                                                                                          |
| ↔        |                    |                                                                                                                                                                          |
| ⬆        |                    |                                                                                                                                                                          |
| ⬇        |                    |                                                                                                                                                                          |
| ∑        | sigma              |                                                                                                                                                                          |
| ⊗        |                    |                                                                                                                                                                          |
| ∈        |                    |                                                                                                                                                                          |
| ∉        |                    |                                                                                                                                                                          |
| ⍳        |                    |                                                                                                                                                                          |
| ∩        |                    |                                                                                                                                                                          |
| ∪        |                    |                                                                                                                                                                          |
| ⊖        |                    |                                                                                                                                                                          |
| ⊛        |                    |                                                                                                                                                                          |
| Δ        |                    |                                                                                                                                                                          |
| ⌀        |                    |                                                                                                                                                                          |
| κ        |                    |                                                                                                                                                                          |
| ρ        |                    |                                                                                                                                                                          |
| χ        |                    |                                                                                                                                                                          |
| ≡        |                    |                                                                                                                                                                          |
| ‾        |                    |                                                                                                                                                                          |
| _        |                    |                                                                                                                                                                          |
| ⋃        |                    |                                                                                                                                                                          |
| ✂        |                    |                                                                                                                                                                          |
| +        |                    |                                                                                                                                                                          |
| -        |                    |                                                                                                                                                                          |
| ×        |                    |                                                                                                                                                                          |
| ÷        |                    |                                                                                                                                                                          |
| %        |                    |                                                                                                                                                                          |
| ⁻        |                    |                                                                                                                                                                          |
| ∥        |                    |                                                                                                                                                                          |
| ⊡        |                    |                                                                                                                                                                          |
| τ        |                    |                                                                                                                                                                          |
| ⌂        |                    |                                                                                                                                                                          |
| ⊤        |                    |                                                                                                                                                                          |
| ⊞        |                    |                                                                                                                                                                          |
| ν        |                    |                                                                                                                                                                          |
