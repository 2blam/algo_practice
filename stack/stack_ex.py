def is_matched(expression):
    stack = []
    for c in expression:
        if c in ['(', '[', '{']: #push
            stack.append(c)
        else:
            if (len(stack) == 0):
                return False
            top = stack.pop()
            if (c == ')' and top =='(') or (c == ']' and top == '[') or (c == '}' and top == '{'):
                continue
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


expression = "{{[[(())]]}}"
if is_matched(expression) == True:
    print("YES")
else:
    print("NO")
