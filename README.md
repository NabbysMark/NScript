# Naco Script

Yes, it pains me to use this language too.

# Installation

On windows, install the zip file, extract it and then you have to copy the path, put it in your environment variables.

You can check if this worked by running `nacoscript -v` in Windows Powershell.

# How to compile a new version of nacoscript if you

run python -m PyInstaller --onefile nacoscript.py  
if you wanna build a new version of this, or if you've modified the code  
to add something new.

# Documentation

## Basic Syntax

```nacoscript
YE x BOOM 10
FELLA "Hello, World!"
WHAT (x IS 10) WE
    FELLA "x is ten"
POW
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

## More Resources

For more examples and advanced usage, see the `nscript_libs` folder and explore the built-in libraries.
