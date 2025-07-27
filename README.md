# Naco Script

Yes, it pains me to use this language too.

# Installation

On windows, install the zip file, extract it and then you have to copy the path, put it in your environment variables.

You can check if this worked by running `nacoscript -v` in Windows Powershell.

## Linux Support

1. **Extract the files** to a directory, e.g., `~/NacoScript`.
2. **Add the directory to your PATH**:
   ```sh
   export PATH="$PATH:$HOME/NacoScript"
   ```
   Add this to your `.bashrc`, `.zshrc`, or equivalent for persistence.
3. **Run scripts** using:
   ```sh
   python3 nacoscript.py yourscript.n
   ```
   or make `nacoscript.py` executable:
   ```sh
   chmod +x nacoscript.py
   ./nacoscript.py yourscript.n
   ```
4. **Check version**:
   ```sh
   ./nacoscript.py -v
   ```

> **Note:**  
> On Linux, the library folder is stored in `~/.local/share/nscript_libs` instead of `%LOCALAPPDATA%\nscript_libs`.  
> Make sure your interpreter uses the correct path for Linux (see below).

# Building from Source

1. Clone the Repostiory

2. run `python -m PyInstaller --onefile nacoscript.py`

# Documentation

## Basic Syntax

```nacoscript
YE x BOOM 10
FELLA "Hello, World!"
@
WHAT (x IS 10) WE
    FELLA "x is ten"
POW
@
```

## Keywords

- `YE` - Declare a variable
- `BOOM` - Assignment operator
- `FELLA` - Print to output
- `WHAT` - If statement
- `WE ... POW` - Block delimiters
- `SPIN` - For loop
- `WAITING` - While loop
- `POPPIN` - Function definition
- `RETURN` - Return from function
- `GIVE LIBRARY "libname"` - Import a Python library
- `GIVE ME "file"` - Import a NacoScript file
- `AS` - Import with alias
- `BUT ONLY` - Import only a specific function/variable/class
- `KILL SELF` - Terminate the script
- `SUPERMAN` - Call superclass constructor in class extending

## Functions

```nacoscript
POPPIN add(a, b)
    RETURN a + b
POW

YE result BOOM add(2, 3)
FELLA result
```

## Using Python Libraries

To use a Python library, place it in  
`%LOCALAPPDATA%\nscript_libs\libname\main.py` and import it:

```nacoscript
GIVE LIBRARY "math"
FELLA math.sqrt(16)
```

All top-level functions and variables in `main.py` are accessible as `math.function()`.

### Import with alias and selective import

```nacoscript
GIVE LIBRARY "math" AS mlib BUT ONLY sqrt
FELLA mlib(16)
```

## Using NacoScript Modules

```nacoscript
GIVE ME "utils" AS u BUT ONLY helper
FELLA u("test")
```

Or import all as a namespace:

```nacoscript
GIVE ME "utils" AS u
FELLA u.helper("test")
```

## Passing Functions as Arguments

```nacoscript
POPPIN sayHello(name)
    FELLA "Hello, " FEED name
POW

POPPIN callTwice(func, arg)
    func(arg)
    func(arg)
POW

callTwice(sayHello, "Adrian")
```

## Comments

```nacoscript
// This is a comment
```

## String Interpolation

```nacoscript
YE name BOOM "Adrian"
FELLA `Hello ${name}!`
```

## Classes and Extending

```nacoscript
LEARNING Person WE
    POPPIN constructor(ts, name, age)
        ts.name BOOM name
        ts.age BOOM age
    POW

    POPPIN greet(ts)
        FELLA `Hello, my name is ${ts.name} and I am ${ts.age} years old.`
    POW
POW

EXTENDING Person WITH Student WE
    POPPIN constructor(ts, name, age, school)
        SUPERMAN(name, age)
        ts.school BOOM school
    POW

    POPPIN greet(ts)
        FELLA `Hi, I'm ${ts.name}, ${ts.age} years old, and I go to ${ts.school}.`
    POW
POW

YE s BOOM BUILD Student("Alice", 13, "Elmore Elementary")
s.greet()
```

## Checking Expressions (Comparisons & Logic)

- `IS` - Equality check: `WHAT (x IS 10)`
- `IS NOT` or `ISNOT` - Inequality check: `WHAT (x IS NOT 5)`
- `IS UNDER` - Less than: `WHAT (x IS UNDER 100)`
- `IS OVER` - Greater than: `WHAT (x IS OVER 0)`
- `ALSO` - Logical AND: `WHAT (x IS 10 ALSO y IS 20)`
- `MAYBE` - Logical OR: `WHAT (x IS 10 MAYBE y IS 20)`
- `NOT` - Logical NOT: `WHAT (NOT x IS 5)`
- `ANOTHER` - Else block: `ANOTHER WE ... @ ... @`
- `ANOTHER ONE` - Else if block: `ANOTHER ONE (condition) WE ... @ ... @`

```nacoscript
@
WHAT (x IS 10 ALSO y IS OVER 5) WE
    FELLA "x is 10 and y is greater than 5"
POW

ANOTHER ONE (x IS 10 MAYBE y IS 20) WE
    FELLA "x is 10 or y is 20"
POW

ANOTHER WE
    FELLA "Neither condition matched"
POW
@
```

## Typechecking

You can declare variable types and function return types for type safety.

### Variable Typechecking

Declare a variable with a type using a colon after the name:

```nacoscript
YE myStr: string BOOM "Hello!"
YE myNum: num BOOM 42
YE myBool: bool BOOM true
YE myList: list BOOM [1, 2, 3]
YE myDict: dict BOOM {"a": 1}
```

If you assign a value of the wrong type, you will get a type error:

```nacoscript
YE myStr: string BOOM 123      // Type error!
```

#### Union Types

You can allow multiple types using `/`:

```nacoscript
YE myVar: string / num BOOM "hi"
myVar BOOM 123      // OK
myVar BOOM [1,2,3]  // Type error!
```

Supported built-in types: `string`, `num`, `bool`, `list`, `dict` (and aliases: `str`, `number`, `boolean`, `array`, `dictionary`, `int`, `float`).

#### Custom Types

You can use class names as types:

```nacoscript
LEARNING Person WE
    POPPIN constructor(ts, name) WE
        ts.name BOOM name
    POW
POW

YE p: Person BOOM BUILD Person("Ada")
FELLA TYPEOF p      // prints "Person"
```

### Function Return Typechecking

You can specify what type a function must return using `WE: type`:

```nacoscript
POPPIN getstr() WE: string
    RETURN "I return a string!"
POW

POPPIN makeperson(name) WE: Person
    RETURN BUILD Person(name)
POW

YE p: Person BOOM makeperson("Ada")
```

### Type Errors

```nacoscript
YE myNum: num BOOM "not a number"   // Type error!
POPPIN bad() WE: string
    RETURN 123                      // Type error!
POW
```

### Typeof Usage

```nacoscript
YE myList: list BOOM [1, 2, 3]
FELLA TYPEOF myList    // prints "list"

LEARNING Animal WE
    POPPIN constructor(ts, name) WE
        ts.name BOOM name
    POW
POW
YE a: Animal BOOM BUILD Animal("Dog")
FELLA TYPEOF a         // prints "Animal"
```

## More Resources

For more examples and advanced usage, see the `nscript_libs` folder and explore the built-in libraries.
