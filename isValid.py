def isValid(s):
    stack = []

    pairs = {')': '(', ']': '[', '}': '{'}

    for p in s:
        if p in '([{':
            stack.append(p)
        else:
            if not stack:
                return False
            if stack[-1] == pairs[p]:
                stack.pop()
            else:
                return False
    return not stack

print(isValid('([{}])'))
print(isValid("(]"))