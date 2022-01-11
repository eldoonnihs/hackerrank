#!/bin/python

from abc import abstractmethod
import math
import os
import random
import re
import sys

def fizzbuzz(n):
    for i in range(n):
        if (i+1)%15==0:
            print ("FizzBuzz")
        elif (i+1)%3==0 and (i+1)%5!=0:
            print ("Fizz")
        elif (i+1)%3!=0 and (i+1)%5==0:
            print ("Buzz")
        else:
            print(i+1)

def min_num(A, K, P):
    Asha = P
    Kelly = 0
    num = 0
    while Kelly <= Asha:
        num += 1
        Asha += A
        Kelly += K
    return num
        
def count_holes(num):
    zero = ["1","2","3","5","7"]
    one = ["0","4","6","9"]
    two = ["8"]
    numstring = str(num)
    holes = 0
    for i in num:
        if i in one:
            holes += 1
        elif i in two:
            holes += 2
    return holes

# def last_stone_weight(a):
#     a.sort()
#     while len(a)>1:
#         if (a[len(a)-1] - a [len(a)-2]) == 0:
#             del a[-2:-1]
#         elif (a[len(a)-1] - a [len(a)-2]) > 0:
#             a[len(a)-1] = (a[len(a)-1] - a [len(a)-2])
#             a.pop(len(a)-2)
#             a.sort()
#     if a:
#         return a.pop(0)
#     else:
#         return 0
    
def last_stone_weight(a):
    # a.sort()
    while len(a)>1:
        if (a[-1] == a [-2]):
            a.pop()
            a.pop()
        else:
            a[-2] = abs(a[-1]-a[-2])
            # print(temp)
            # print("a[-1]=",a[-1]," a[-2]=",a[-2])
            # a[-2] = temp
            
            a.pop()
        print(a)    
    if a:
        return a.pop(0)
    else:
        return 0


def anagram(a, b):
    if len(a) != len(b):
        return -1
    set_a = set(a)
    set_b = set(b)
    difference = set_a.symmetric_difference(set_b)
    print (difference)
    if difference:
        return int(len(difference)/2)
    else:
        return 0

def reducedFractionSums(a,b,c,d):
    small = 0
    big = 0
    if b%d == 0:
        ac = a + int(c*(b/d))
        bd = b
    elif d%b == 0:
        ac = int(a*(d/b)) + c
        bd = d
    else:
        ac = a*d + c*b
        bd = b*d
    if ac == bd:
        return f"The expression {a}/{b} + {c}/{d} evaluates to {ac}/{bd}, which we reduce to the string 1/1"
    elif ac > bd:
        small = bd
        big = ac
    elif ac < bd:
        small = ac
        big = bd
   
    while small != 0:
        t = small
        small = big % small
        big = t
    e = int(ac / big)
    f = int(bd / big)
    return f"The expression {a}/{b} + {c}/{d} evaluates to {ac}/{bd}, which we reduce to the string {e}/{f}"

def cardPackets(cardTypes): 
    two = 0
    three = 0
    for i in cardTypes:
        if i % 2 != 0:
            two += 1
        if i % 3 == 2:
            three += 1
        if i % 3 == 1:
            three += 2
    return 

if __name__ == '__main__':
    
    x = lastStoneWeight
    # result=last_stone_weight([7,6,7,6,9])
    # print(result)
    # 1,2,3,4,5,6,7,8,9
    # n = int(input("enter an integer: ").strip())
    # fizzbuzz(n)
    
    # n = int(input("enter an integer").strip())

    # if n%2 != 0: 
    #     print("weird")
    # else:
    #     if (n >= 2) and (n <= 5):
    #         print ("not weird")
    #     elif (n >= 6) and (n <= 20):
    #         print("weird")
    #     elif (n > 20):
    #         print ("not weird")
    # a = int(input("first integer: "))
    # b = int(input("second integer: "))


#   Minion Game
    # a = input("any string: ").upper()
    # cons = 0
    # vow = 0
    # vowels = 'AEIOU'
    # for i in range( len(a) ):
    #     if a[i] in vowels:
    #         vow += len(a) - i
    #     else:
    #         cons += len(a) - i
    # if cons > vow:
    #     print ("Stuart ", cons)
    # elif cons == vow:
    #     print ("Draw")
    # else:
    #     print ("Kevin ", vow)