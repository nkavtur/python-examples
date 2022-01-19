import os
import statistics
import sys

import fibo_mobule

# The os module provides dozens of functions for interacting with the operating system:

print(os.getcwd())  # current working directory
os.chdir('test') # change working directory

# os.system('mkdir test')  # system command

# low-level IO
# opens file for appending. Appends bytes to the end of file
# fd = os.open(path="foo.text", flags=os.O_CREAT | os.O_WRONLY | os.O_APPEND)

# opens file for writing. overwrites from the beginning to n bytes written
fd = os.open(path="foo.text", flags=os.O_CREAT | os.O_WRONLY)

# write to the beginning
os.write(fd, "privet mir\n".encode())

# write to end
os.lseek(fd, 0, os.SEEK_END)
os.write(fd, "Privet!\n".encode())

os.close(fd)

print(dir(fibo_mobule))  # show the list of names in the current local scope
help(fibo_mobule)  # show help

# For daily file and directory management tasks, the shutil module provides a higher level
# interface that is easier to use:
import shutil

shutil.copy('foo.text', 'bar.text')
# shutil.move(f'bar.text', 'baz.text')


# The glob module finds all the pathnames matching a specified pattern
import glob

print(glob.glob('*.text'))

# possible to write to stderr, stdout directly
sys.stderr.write('some error\n')
sys.stdout.write('some output\n')

# Mathematics
import math, random

print(math.sin(math.pi / 2))

print(random.choice([1, 2, 3]))

sample1 = random.sample(range(10), 9)
sample2 = random.sample(range(10), 9)
sample3 = random.sample(range(10), 9)


def win1(*samples, nrange=9, max_n=10):
    final_res = []
    for sample in samples:
        sample_res = []
        for n in sample:
            if n >= (max_n / 2):
                sample_res.append(n)
        if len(sample_res) >= (nrange // 2 + 1):
            final_res.append("yes")
        else:
            final_res.append("no")
    return final_res


def win2(*samples, nrange=9, max_n=10):
    filtered = [
        [n for n in sample if n >= max_n / 2]
        for sample in samples
    ]
    return ["yes" if len(f) >= (nrange // 2 + 1) else "no" for f in filtered]


def win3(*samples, nrange=9, max_n=10):
    medians = [
        statistics.median(sample)
        for sample in samples
    ]
    return ["yes" if m >= (max_n / 2) else "no" for m in medians]


print(win1(sample1, sample2, sample3))
print(win2(sample1, sample2, sample3))
print(win3(sample1, sample2, sample3))
