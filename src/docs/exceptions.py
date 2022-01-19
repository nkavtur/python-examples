# ex1: except multiple exceptions
try:
    int('ha')
except (RuntimeError, TypeError, NameError, ValueError):
    print("Oops! something went wrong")


# ex2: exception hierarchy
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# ex3: default except
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# try-except-else block
for arg in sys.argv[1:]:
    try:
        file = open(arg, 'r')
    except IOError:
        print('cannot open file', arg)
    else:
        print(f"number of lines {len(file.readlines())} in {arg}")


# ex4: exception internals

try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(type(e))
    print(str(e))
    print(e.args)
    x, y = e.args
    print(x, y)

# ex5: re-raise error
try:
    raise NameError('hello', 'hi')
except NameError as e:
    print(f"got error {type(e)}{e}")
    # raise


# ex6: exception channing
try:
    raise ValueError('first')
except ValueError as e:
    print(f"got following exception: {e}")
    # raise Exception('second') from e


# ex7: finally
try:
    1 + 1
    # raise Exception('e')
finally:
    print('Good Bie!')

# ex7: close file automatically
with open("exceptions.py") as f:
    for line in f:
        print(line, end="")
