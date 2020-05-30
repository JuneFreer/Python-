# 中缀表达式转后缀表达式

from stack import Stack

def infixToPostfix(infixexpr):
    prec = {} # 优先级
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split() # 默认用空格split

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ''.join(postfixList) # 列表转字符串


if __name__ == '__main__':
    infix = '( ( ( A + B ) * C ) + D )'
    postfix = infixToPostfix(infix)
    print(postfix)
