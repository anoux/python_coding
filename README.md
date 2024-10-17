# Basic Python knowledge.

## Key Concepts

### Constant
A fixed value such as numbers, letters and strings

### Reserved words
Those you can not use as identifiers (variable names) for constants

### Variable
A named place in the memory where a programmer can store data and later retrieve the data using the varaible name (identifier)

Rules for varaibles names: only start with letter or underscore and they are case sensitive

### Data types

- integer
- float (is dominating in presence of an integer)
- string

### Some functions
- `input()` makes Python read data from the user
- `type()` returns data type
- `int() str() float()` coverts data type to another type. The use of these is limited to logical conversions, e.g. the following `int('hello there')` returns an error
- `dir()` returns an alphabetically sorted list containing all entities' names available in a module given as argument. e.g. `dir(math)`. Before using it, the module must have been already imported.

### Modules
- A module is a file containing Python definitions and statements. Each module consists of entities (functions, variables, constants, classes, and objects).
- A module user is the one that uses an existing module, meanwhile the module supplier is the one who creates a brand new module.
- A large number of modules is delivered together with Python itself. All these modules, along with the built-in functions, form the Python standard library.
- To make a module usable, it must be imported by using the `import` keyword followed by the module's name. If only a certain entity or entities from a module are wanted to import, then `from module import entity`. e.g. `from math import pi`.

### Packages
- A package is a set of modules. The presence of the __init.py__ file finally makes up the package.

### Dependencies
Adependency is a phenomenon that appears every time you're going to use a piece of software that relies on other software.
`pip` can discover, identift and resolve all dependencies
