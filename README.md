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

Also, there is a function called type() which returns the data type of a variable as well as there are the functions int(), float() and str() to convert a variable to one or another type. Anymay, the use of these is limited to logical conversions, e.g. the following `int('hello there')` returns an error

### Some functions
- input() makes Python read data from the user
- type() returns data type
- int() str() float() coverts data type to another type

### Modules
- A module is a file containing Python definitions and statements. Each module consists of entities (functions, variables, constants, classes, and objects).
- A module user is the one that uses an existing module, meanwhile the module supplier is the one who creates a brand new module.
- A large number of modules is delivered together with Python itself. All these modules, along with the built-in functions, form the Python standard library.
- To make a module usable, it must be imported by using the `import` keyword followed by the module's name.
