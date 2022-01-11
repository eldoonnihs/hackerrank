def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    return int(meal_cost*(1+tip_percent/100+tax_percent/100))

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)