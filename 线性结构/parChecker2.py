# 更广义的括号匹配，stack

from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        if symbolString[i] in '([{':
            s.push(symbolString[i])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbolString[i]): # matches函数是一个小trick
                    balanced = False
        i += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close): # matches函数是一个小trick
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

# 注意，整个程序中，右括号始终不会进栈
