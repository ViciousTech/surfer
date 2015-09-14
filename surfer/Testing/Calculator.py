
import math

def if_operand(lest):
        operands  = ['+','-','*','x','/','^','(',')']
        for opers in operands:
            if(lest == opers):return True
        return False
def calculates(a,b,sign):
    a = int(a);b = int(b)
    if(sign == '*'): return (a * b)
    elif(sign == '-'): return (a - b)
    elif(sign == '+'): return (a + b)
    elif(sign == '/'): return (a / b)
    elif(sign == '^'): return int(math.pow(a,b))

class Calc_num:
    def __init__(self):
        self.oper = []
    def convert(self,inputs):
        _1 = str(inputs).split();z=0;listindex = 0;i=0
        temper = ''.join(_1)
        self.oper = [None] * int(temper.__len__())
        while(temper.__len__() > i):
            if(if_operand(temper[i])):
                self.oper[listindex] = temper[z:i]
                listindex = listindex + 1
                self.oper[listindex] = temper[i];z = i+1
                listindex =  listindex + 1
            self.oper[listindex] = temper[z:i+1]
            i = i + 1
test = Calc_num()
vi = input("Enter the Calculation String" + '\n')
test.convert(vi);
i = 0;popper =0
while True:
    if(if_operand(test.oper[i])):
        val = calculates(test.oper[i-1],test.oper[i+1],str(test.oper[i]))
        test.oper.pop(popper);
        popper = popper +1
        test.oper.pop(popper)
        popper = 0
        test.oper[0] = val
        i = 0
    i = i + 1
    if(i > test.oper.__len__() - 1): break
print(val)