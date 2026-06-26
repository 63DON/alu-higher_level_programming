# python-import_modules

## ALU - Higher Level Programming

This project covers how to import functions and variables from Python modules, and how to use `sys.argv` to handle command-line arguments.

## Learning Objectives

- How to import functions from another file
- How to import variables from another file
- How to use `sys.argv` to print command-line arguments
- How to know the number of arguments passed to a script
- What is and what is the goal of `if __name__ == "__main__"`
- How to find all hidden attributes of a module with `dir()`

## Requirements

- All scripts are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code is validated against pycodestyle (version 2.8.*)
- All files must be executable
- A `README.md` file at the root of the project is mandatory

## Tasks

| File | Description |
| --- | --- |
| `add_0.py` | Module containing the `add` function |
| `0-add.py` | Imports `add` from `add_0` and prints the result of an addition |
| `calculator_1.py` | Module containing `add`, `sub`, `mul` and `div` functions |
| `1-calculation.py` | Imports all four functions from `calculator_1` and prints results |
| `2-args.py` | Prints the number of and value of arguments passed to the script |
| `3-infinite_add.py` | Prints the sum of all integer arguments passed to the script |
| `4-hidden_discovery.py` | Prints the names of all attributes of `hidden_4` that do not start with `__` |
| `variable_load_5.py` | Module containing a variable `a` |
| `5-variable_load.py` | Loads variable `a` from `variable_load_5` using `__import__` |
