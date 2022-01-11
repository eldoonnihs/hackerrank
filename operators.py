import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total = round(meal_cost*(1.00+tip_percent/100.00+tax_percent/100.00))
    print (int(total))

if __name__ == '__main__':
    # strip is only necessary if you are taking the inputs in the form of string 
    # meal_cost = float(input().strip())
    # tip_percent = int(input().strip())
    # tax_percent = int(input().strip())
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    # float(meal_cost)
    # int(tip_percent)
    # int(tax_percent)

    print (meal_cost, tip_percent, tax_percent)
    print (1+float(tip_percent/100.00)+float(tax_percent/100.00))
    print (float(tip_percent/100.00))
    print (float(tax_percent/100.00))
    solve(meal_cost, tip_percent, tax_percent)