# 括号匹配，stack

from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        if symbolString[i] == '(':
            s.push(symbolString[i])
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))
