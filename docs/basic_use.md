# Basic use

Circl can be executed in two forms, each either with or without a given expression as a command line argument.
This expression should be a valid Circl expression, e.g. `"Hello, World!"^.`

- **Package:** install the `circl` package and run it
```shell
pip install .
circl [expression]

# example:
circl "Hello, World!"^.
```
- **Standard command:** run directly using `python`
```shell
pip install .
python -m circl [expression]

# example:
python -m circl "Hello, World!"^.
```
