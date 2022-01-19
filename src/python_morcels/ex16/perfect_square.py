import decimal
from decimal import Decimal
from typing import Union


# way1
def is_perfect_square(n: Union[int, float, Decimal]):
    if n < 0:
        return False
    return '.' not in str(Decimal(n).sqrt() % 1)


assert is_perfect_square(64)
assert not is_perfect_square(65)
assert is_perfect_square(100)
assert not is_perfect_square(1000)
assert is_perfect_square(Decimal(100))
assert not is_perfect_square(-1)
assert not is_perfect_square(-4)
assert is_perfect_square(4624000000000000)
assert not is_perfect_square(4623999999999999)

# way2
from decimal import Inexact
import cmath


def is_perfect_square(n: Union[int, float, Decimal, complex], *, complex=False):
    if complex:
        _s = cmath.sqrt(n)
        return _s.real % 1 == 0 and _s.imag % 1 == 0

    else:
        if n < 0:
            return False

        with decimal.localcontext() as ctx:
            ctx.traps[Inexact] = True

            try:
                res = Decimal(n).sqrt()
            except Inexact:
                return False

            return res % 1 == 0


assert is_perfect_square(64)
assert not is_perfect_square(65)
assert is_perfect_square(100)
assert not is_perfect_square(1000)
assert is_perfect_square(Decimal(100))
assert not is_perfect_square(-1)
assert not is_perfect_square(-4)
assert is_perfect_square(4624000000000000)
assert not is_perfect_square(4623999999999999)
assert is_perfect_square(512j, complex=True)
assert not is_perfect_square(513j, complex=True)


# way3
def is_perfect_square(n: Union[int, float, Decimal, complex], *, complex=False):
    if complex:
        _s = cmath.sqrt(n)
        return _s.real % 1 == 0 and _s.imag % 1 == 0

    else:
        if n < 0:
            return False

        with decimal.localcontext() as ctx:
            ctx.clear_flags()

            res = Decimal(n).sqrt()
            if ctx.flags[Inexact]:
                return False

            return res % 1 == 0


assert is_perfect_square(64)
assert not is_perfect_square(65)
assert is_perfect_square(100)
assert not is_perfect_square(1000)
assert is_perfect_square(Decimal(100))
assert not is_perfect_square(-1)
assert not is_perfect_square(-4)
assert is_perfect_square(4624000000000000)
assert not is_perfect_square(4623999999999999)
assert is_perfect_square(512j, complex=True)
assert not is_perfect_square(513j, complex=True)

import string

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : $vars
Escape          : $$
Variable in text: ${var}siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))

print(2**10000)
