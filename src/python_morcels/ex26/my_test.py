from sortutils import natural_key, natural_sort


def reverse_name(name):
    """Key function to sort by last name first."""
    first, last = name.rsplit(' ', 1)
    return natural_key(last + ' ' + first)


# base problem
assert natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar']) == ['hotel', 'India', 'Oscar', 'uncle', 'Yankee', 'zebra']
assert natural_sort(['Uruguay', 'echo', 'Charlie', 'golf']) == ['Charlie', 'echo', 'golf', 'Uruguay']
assert natural_sort(['Uruguay', 'echo', 'Charlie', 'golf'], reverse=True) == ['Uruguay', 'golf', 'echo', 'Charlie']

# bonus 1
assert natural_sort(['McDonald', 'MCDONALD', 'Mcdonald', 'MacDonald']) == ['MacDonald', 'McDonald', 'MCDONALD', 'Mcdonald']

names = ['Sarah Clarke', 'Sara Hillard', 'Sarah Chiu']
assert natural_sort(names, key=reverse_name) == ['Sarah Chiu', 'Sarah Clarke', 'Sara Hillard']
assert natural_sort(names) == ['Sara Hillard', 'Sarah Chiu', 'Sarah Clarke']

# bonus 2
assert natural_sort(['my 13 cats', 'your 1 pig', 'my 2 dogs', 'your 16 squirrels']) == ['my 2 dogs', 'my 13 cats', 'your 1 pig', 'your 16 squirrels']

# bonus 3
from pathlib import Path
from sortutils import natural_key


@natural_key.register(Path)
def natural_path_key(path):
    return [natural_key(part) for part in path.parts]


paths = [Path('file 1'), Path('file 10'), Path('file 2'), Path('file 3')]
print(*natural_sort(paths), sep="\n")
