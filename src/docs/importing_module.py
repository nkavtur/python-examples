# ex 1
import fibo_mobule
print(fibo_mobule.__name__)
fibo_mobule.fib1(10)
print(fibo_mobule.fib2(10))

# ex 2
from fibo_mobule import fib1, fib2
fib1(10)
print(fib2(10))

# ex 3 (This imports all names except those beginning with an underscore _)
# In most cases Python programmers do not use this
from fibo_mobule import *
fib1(10)

# ex 4
import fibo_mobule as x
x.fib1(10)

# ex 5
from fibo_mobule import fib1 as fib100
fib100(10)


# ex 6
import fibo_mobule
fib1 = fibo_mobule.fib1
fib1(10)


# Note For efficiency reasons, each module is only imported once per interpreter session.
# Therefore, if you change your modules, you must restart the interpreter – or,
# if it’s just one module you want to test interactively, use importlib.reload(),
# e.g. import importlib; importlib.reload(modulename).

# When a module named spam is imported, the interpreter first searches for a built-in module with that name.
#  If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.

# Now what happens when the user writes `from some.package import *`?
# The only solution is for the package author to provide an explicit index of the package.
# The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__,
# it is taken to be the list of module names that should be imported when from package import * is encountered:
# `__all__ = ["echo", "surround", "reverse"]`
# This would mean that `from some.package import *` would import the three named submodules of the sound package.

# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package
# sound.effects into the current namespace; it only ensures that the package sound.effects has been imported
# (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package.
# This includes any names defined (and submodules explicitly loaded) by __init__.py.
# It also includes any submodules of the package that were explicitly loaded by previous import statements.



from sound import *

echo.echo()

# private method by convention!!!
echo._private_echo()

# does not work, because __all__ contains only echo
# surround.surround()
