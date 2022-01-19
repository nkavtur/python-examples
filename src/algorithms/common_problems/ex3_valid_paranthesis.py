def valid_parentheses(text):
    stack = []

    parentheses_dict = {')': '(', '}': '{', ']': '['}
    for c in text:
        if c not in parentheses_dict:
            stack.append(c)
        else:
            if stack.pop() != parentheses_dict[c]:
                return False
    return True


print(valid_parentheses("()"))
print(valid_parentheses("()[]{}"))
print(valid_parentheses("(]"))
print(valid_parentheses("([)]"))
print(valid_parentheses("{[]}"))
