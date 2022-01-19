# A namespace is a mapping from names to objects.
# Most namespaces are currently implemented as Python dictionaries.
# Examples: built-in functions namespace, module global names, local function variables

# Although scopes are determined statically, they are used dynamically.
# At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:
# the innermost scope, which is searched first, contains the local names
# the scopes of any enclosing functions, contains non-local, but also non-global names
# the next-to-last scope contains the current module’s global names
# the outermost scope (searched last) is the namespace containing built-in names


# The global statement can be used to indicate that particular variables live in the global scope;
# the nonlocal statement indicates that particular variables live in an enclosing scope.


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


# Very important!!!!
# When a class definition is entered, a new namespace is created,
# and used as the local scope — thus, all assignments to local variables go into this new namespace.
# In particular, function definitions bind the name of the new function here.

class Complex:
    x = 'class variable'

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def print(self):
        print(self)

    def __str__(self):
        return f"{self.r} + {self.i} * i"

print(Complex.x)  # class variable
print(Complex(10, -11).r)  # instance variable

x = Complex(-1, 3)
x.print()
Complex.print(x)

# MyClass.f() - class function, comes from class namespace
# x.f - method object.
# x.f() is exactly equivalent to MyClass.f(x).

# Instance method is an abstract type which is combination of instance object itself and class function:
x = Complex(3, 4)
print(x.print.__self__)
print(x.print.__func__)

# attributes are stored in a __dict__ object.
print('dict: ', x.__dict__)

# Generally speaking, instance variables are for data unique to each instance
# and class variables are for attributes and methods shared by all instances of the class:
class Dog:
    tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


# If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:
class Warehouse:
    purpose = 'storage'
    region = 'west'
    list = []


w1 = Warehouse()
w2 = Warehouse()

w2.region = 'east'
print(w1.purpose, w1.region, w1.list)
print(w2.purpose, w2.region, w2.list)

w1.list.append(1)
print(w1.purpose, w1.region, w1.list)
print(w2.purpose, w2.region, w2.list)


# class function can be defined outside the class:
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


# Methods may reference global names in the same way as ordinary functions.
# The global scope associated with a method is the module containing its definition not class!!!

# Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.


# Inheritance:
class BaseClass1:
    def hello(self):
        print("Hello 1")


class BaseClass2:
    def hello(self):
        print("Hello 2")


class ChildClass(BaseClass1, BaseClass2):
    def hello(self):
        BaseClass2.hello(self) # to call super class
        print("Hi")


ChildClass().hello()


# Private variables don't exist in python. However there's convention:
# a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API


# Since there is a valid use-case for class-private members,
# there is limited support for such a mechanism, called name mangling.
# Any identifier of the form __spam is textually replaced with _classname__spam,
# where classname is the current class name with leading underscore(s) stripped.
# This mangling is done without regard to the syntactic position of the identifier,
# as long as it occurs within the definition of a class.

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# The above example would work even if MappingSubclass were to introduce a __update identifier,
# since it is replaced with _Mapping__update in the Mapping class and _MappingSubclass__update in the MappingSubclass.


x = MappingSubclass([1, 2, 3])
print(x.items_list)

x.update([4, 5, 6], ["a", "b", "c"])
print(x.items_list)


# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”,
# bundling together a few named data items. An empty class definition will do nicely:

class Employee:
    pass


john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# How iterators work:
for x in [1, 2, 3]:
    print(x)

it = iter([1, 2, 3])
print(it.__next__())  # iterator.__next__ is equivalent for next() from builtins
print(next(it))
print(next(it))


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        val = self.data[self.index]
        self.index -= 1
        return val


for x in Reverse([1, 2, 3]):
    print(x)


# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement whenever they want to return data
# after performing yield it preserves current intermediate state and continues on __next__ method.
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for x in reverse([1, 2, 3]):
    print(x)

# Generator expression.
# Generator expressions are more compact but less versatile than full generator definitions
# and tend to be more memory friendly than equivalent list comprehensions.
sum(i * i for i in range(10))
gen = (i * i for i in range(1000000))  # it won't be executed directly

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
