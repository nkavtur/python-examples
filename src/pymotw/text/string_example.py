import string

# capwords
from typing import Any, Tuple

s = 'hello world tEST'
assert string.capwords(s) == 'Hello World Test'

# template examples:
mapping = {'var': 'foo'}

# 1. string.Template
t = string.Template("""
    Variable: $var
    Escape: $$
    Variable in text ${var}iable
""")
assert t.substitute(mapping) == """
    Variable: foo
    Escape: $
    Variable in text fooiable
"""

t = string.Template("$var is here but $missing is not provided")
try:
    print('substitute()     :', t.substitute(mapping))
except KeyError as err:
    print('ERROR:', type(err))

assert t.safe_substitute(mapping) == "foo is here but $missing is not provided"


class MyTemplate(string.Template):
    delimiter = "+"
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
  Delimiter : ++
  Replaced  : +with_underscore
  Ignored   : +notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced',
}

assert MyTemplate(template_text).safe_substitute(d) == """
  Delimiter : +
  Replaced  : replaced
  Ignored   : +notunderscored
"""

# 2. interpolation
s = """
    Variable        : %(var)s
    Escape          : %%
    Variable in text: %(var)siable
"""
assert s % mapping == """
    Variable        : foo
    Escape          : %
    Variable in text: fooiable
"""

# str.format
s = """
    Variable        : {var}
    Escape          : {{}}
    Variable in text: {var}iable
"""
assert s.format(**mapping) == """
    Variable        : foo
    Escape          : {}
    Variable in text: fooiable
"""

# str builtin template

s = (
    f"Variable        : {mapping['var']}"
    f"Escape          : "
    f"Variable in text: {mapping['var']}iable"
)
assert s == "Variable        : fooEscape          : Variable in text: fooiable"

s = f"""
    Variable        : {mapping['var']}
    Escape          : {{}}
    Variable in text: {mapping['var']}iable
"""
assert s == """
    Variable        : foo
    Escape          : {}
    Variable in text: fooiable
"""

# string constants~
import inspect

for name, value in inspect.getmembers(string, lambda m: isinstance(m, str)):
    if name.startswith('_'):
        continue
    print('%s=%r' % (name, value))
