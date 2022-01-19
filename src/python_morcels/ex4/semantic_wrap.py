# ex1
import argparse
import re
import sys


def semantic_wrap(str):
    return ".\n".join(str.split(". "))


# ex2
def semantic_wrap2(str):
    return re.sub(r"\.\s+", r".\n", str)


# ex3
def semantic_wrap3(str):
    return str.replace(". ", ".\n")


# ex4
# def semantic_wrap(str):
#     return re.sub("(\"?[.?!])( +)", r"\1\n", str)
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='semantic wrapping for txt file')
#     parser.add_argument('-f', '--file', help='text file')
#     args = parser.parse_args(sys.argv[1:])
#
#     with open(file=args.file, mode='r') as f:
#         for line in f:
#             sys.stdout.write(semantic_wrap(line))


# ex5
from pathlib import Path


def semantic_wrap(str):
    return re.sub("(\"?[.?!])( +)", r"\1\n", str)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='semantic wrapping for txt file')
    parser.add_argument('-f', '--file', type=Path, help='text file')
    args = parser.parse_args(sys.argv[1:])
    sys.stdout.write(semantic_wrap(args.file.read_text()))
