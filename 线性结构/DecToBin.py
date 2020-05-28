# 十进制转二进制, stack
from stack import Stack

def divideBy2(decNum):
    remstack = Stack()

    while decNum > 0:
        rem = decNum % 2
        remstack.push(rem)
        decNum //= 2

    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString

print(divideBy2(int(input('put a dec number: '))))
