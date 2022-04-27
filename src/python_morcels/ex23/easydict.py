from collections import UserDict
from typing import Any


class EasyDict:

    def __init__(self, properties=None, normalize=False, **kw):
        self._normalize = normalize
        self.__dict__.update({
            self.normalize_key(k): v
            for k, v in {**(properties or dict()), **(kw or dict())}.items()})

    def __getitem__(self, item):
        return getattr(self, self.normalize_key(item))  # getattr - gets from __dict__

    def __setitem__(self, key, value):
        return setattr(self, self.normalize_key(key), value)  # setattr - gets from __dict__

    def get(self, key, default=None):
        return getattr(self, self.normalize_key(key), default)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def normalize_key(self, value: str):
        return value.replace(' ', '_') if self._normalize else value


mydict = EasyDict({'a': 1, 'b': 2})
print(mydict.a)
print(mydict['b'])

# Alternative solution using UserDict class
# The UserDict class has a data attribute that stores the actual data this dictionary-like class by default.
# We're using properties to ensure that this data attribute is really just an alias for the __dict__ attribute
from collections import UserDict


class EasyDict(UserDict):

    def __init__(self, mapping={}, normalize=False, **kwargs):
        self._normalize = normalize
        self.update(mapping) # update from the UserDict class
        self.update(kwargs)

    @property
    def data(self):
        return self.__dict__

    def normalized(self, key):
        return key.replace(' ', '_') if self._normalize else key

    def __getitem__(self, key):
        return self.__dict__[self.normalized(key)]

    def __setitem__(self, key, value):
        self.__dict__[self.normalized(key)] = value
