# 更广义的括号匹配([{}])，stack

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
                balanced = False # 右括号多了
            else:
                top = s.pop()
                if not matches(top, symbolString[i]):  # 左右括号不是同类型
                    balanced = False
        i += 1

    if balanced and s.isEmpty(): # 遍历完栈不为空说明左括号多了
        return True
    else:
        return False

# matches函数是一个小trick
def matches(open, close): # matches函数是一个小trick
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

# 注意，整个程序中，右括号始终不会进栈，它只是用来抵消栈中的左括号(而且抵消的次序是反转的，非常符合栈的特性)
