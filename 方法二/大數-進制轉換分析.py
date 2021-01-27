# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

from itertools import dropwhile
from functools import reduce

class BigInt:
    def __init__(self, val):
        self.value = BigInt.parse(val) if isinstance(val, str) else val
        
    def __str__(self):
        v = BigInt.toComplement(self.value) \
                if BigInt.isNegative(self.value) else self.value
        builder = ['%04d' % v[i] for i in range(len(v) - 1, -1, -1)]
        clist = list(dropwhile(lambda c: c == '0', list(''.join(builder))))
        return '0' if len(clist) == 0 else ''.join(
              ((['-'] + clist) if BigInt.isNegative(self.value) else clist))
        
    def __add__(self, that):
        return (self - BigInt(BigInt.toComplement(that.value))) \
                if BigInt.isNegative(that.value) else self.add(that)
            
    def add(self, that):            
        length = max(len(self.value), len(that.value))
        op1 = BigInt.copyOf(self.value, length)
        op2 = BigInt.copyOf(that.value, length)
        sum = BigInt.addForEach(op1, op2, 0)
        return BigInt(
            (((sum[0:-1] + [1]) if BigInt.isPositive(op1) else []) + [0] * 8)
                if sum[-1] == 1 
                else (sum[0:-1] + [0 if BigInt.isPositive(op1) else 9999])
        )
        
    def __sub__(self, that):
        return (self + BigInt(BigInt.toComplement(that.value))) \
            if BigInt.isNegative(that.value) else self.sub(that)
        
    def sub(self, that):
        length = max(len(self.value), len(that.value))
        op1 = BigInt.copyOf(self.value, length)
        op2 = BigInt.copyOf(that.value, length)        
        remain = BigInt.subForEach(op1, op2, 0)
        return BigInt(
            ((remain[0:-1] + [9998] if BigInt.isNegative(op1) else []) 
                + [9999] * 8) if remain[-1] == 1 
                    else (remain[0:-1] + 
                        [9999 if BigInt.isNegative(op1) else 0])
        )
    
    def multiply(self, val, shift):
        product = [0] * shift + \
            BigInt.multiplyForEach(self.value, val, 0)
        return BigInt((product[0:-1] + product[-1:] + [0] * 8) \
            if product[-1] != 0 else (product[0:-1] + [0]))

    def __mul__(self, that):
        op1 = BigInt(BigInt.toComplement(self.value)) \
                if BigInt.isNegative(self.value) else self
        op2 = BigInt.toComplement(that.value) \
                if BigInt.isNegative(that.value) else that.value
        result = reduce(BigInt.__add__, 
                [op1.multiply(op2[i], i) 
                    for i in range(len(op2) - 1)], BigInt('0'))
        return BigInt(BigInt.toComplement(result.value)) \
                if self.value[-1] + that.value[-1] == 9999 else result

    def __ge__(self, that):
        return False if BigInt.isNegative((self - that).value) else True

    def isLessOrEqualsQuotient(self, op1, op2):
        return True if op1 >= (self * op2) else False
    
    def __floordiv__(self, that):
        op1 = BigInt(BigInt.toComplement(self.value)) \
                if BigInt.isNegative(self.value) else self
        op2 = BigInt(BigInt.toComplement(that.value)) \
                if BigInt.isNegative(that.value) else that
        one = BigInt('1')
        
        def quotient(left, right):
            if right >= left:
                x = (left + right).divide(2)
                l, r = ((x + one, right) 
                    if x.isLessOrEqualsQuotient(op1, op2) 
                    else (left, x - one))
                return quotient(l, r)
            else:
                return left - one
        result = quotient(BigInt('0'), op1)
        return BigInt(BigInt.toComplement(result.value)) \
                if self.value[-1] + that.value[-1] == 9999 else result
    
    @staticmethod
    def divideForEach(op, val, remain):
        if op == []:
            return []
        else:
            tmp = op[-1] + remain
            nextRemain = (tmp % val) * 10000
            return [tmp // val] + \
                BigInt.divideForEach(op[0:-1], val, nextRemain)
    
    def divide(self, that):
        result = BigInt.divideForEach(self.value, that, 0)
        return BigInt(result[::-1] + [0] * (8 - (len(result) % 8)))
        
    @staticmethod
    def parse(val):
        v = val[1:] if val[0] == '-' else val
        digits = [int(v[i if i >= 0 else 0 : i + 4]) 
                for i in range(len(v) - 4, -4, -4)]
        zeros = [0] * ((len(digits) // 8 + 1) * 8 - len(digits))
        return BigInt.toComplement(digits + zeros) \
                if val[0] == '-' else (digits + zeros)

    @staticmethod
    def addForEach(op1, op2, carry):
        if op1 == []:
            return [carry]
        else:
            s = op1[0] + op2[0] + carry
            nextCarry, c = (0, s) if s < 10000 else (1, s - 10000)
            return [c] + BigInt.addForEach(op1[1:], op2[1:], nextCarry)

    @staticmethod
    def subForEach(op1, op2, borrow):
        if op1 == []:
            return [borrow]
        else:
            r = op1[0] - op2[0] - borrow
            nextBorrow, c = (0, r) if r > -1 else (1, r + 10000)
            return [c] + BigInt.subForEach(op1[1:], op2[1:], nextBorrow)

    @staticmethod
    def multiplyForEach(op, val, carry):
        if op == []:
            return [carry]
        else:
            tmp = op[0] * val + carry
            nextCarry = tmp // 10000
            return [tmp % 10000] + \
                    BigInt.multiplyForEach(op[1:], val, nextCarry)
            
    @staticmethod
    def toComplement(v):
        c = [9999 - i for i in v]
        return [c[0] + 1] + c[1:]
    
    @staticmethod
    def copyOf(original, newLength):
        return original + [0 if BigInt.isPositive(original) else 9999 
                for i in range(len(original), newLength)]
    
    @staticmethod
    def isNegative(list):
        return list[-1] == 9999
        
    @staticmethod
    def isPositive(list):
        return list[-1] == 0

def base_analyze(maxln,n):    
    loss_ratio = BigInt('10000')#初始化損失比率的值
    for ln in range(1,maxln+1):
        B_l2 = BigInt(str(int(ln*math.log(n,2)//1)))  #對應的S2長度
        B_ln = BigInt(str(ln))
        B_n = BigInt(str(n))
        B_resultN = BigInt('1')
        for j in range(ln):
            B_resultN = B_resultN*B_n
        B_result2 = BigInt('1')
        for j in range(int(ln*math.log(n,2)//1)):
            B_result2 = B_result2*BigInt('2')
        B_resultSub = B_resultN - B_result2
        B_temp = B_resultSub * BigInt('10000')// B_result2
        print(B_temp)
        if not(B_temp >= loss_ratio) :
            loss_ratio = B_temp
            B_num_ln = B_ln
            B_num_l2 = B_l2
    return B_n,B_num_ln,B_num_l2,loss_ratio
def print_base_analyze(x):
    print("{0}進制".format(x[0]))
    print("ln = "+str(x[1]))
    print("l2 = "+str(x[2]))
    print("loss_ratio = "+str(x[3]))
#主程式        
maxln = 5
n=3
print_base_analyze(base_analyze(maxln,n))
n=5
print_base_analyze(base_analyze(maxln,n))
n=6
print_base_analyze(base_analyze(maxln,n))
n=7
print_base_analyze(base_analyze(maxln,n))
    
    
    