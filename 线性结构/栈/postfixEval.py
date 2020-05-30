# 后缀表达式求值，思路非常简单

from stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split() # 默认用空格分割

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop() # 先弹出的是第二个操作数（为了除法和减法运算）
            operand1 = operandStack.pop() # 后弹出的是第一个操作数
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop() # 最后栈里剩下的一个数，就是求值结果

def doMath(operator, op1, op2):
    if operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2
    elif operator == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    postfix = '3 2 * 5 +'
    result = postfixEval(postfix)
    print(result)
