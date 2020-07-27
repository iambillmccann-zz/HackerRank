# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())  # number of items sold
    daily_sales = OrderedDict()

    for index in range(N):
        item = input().strip()
        split_at = item.rfind(" ")
        item_name = item[:split_at]
        item_price = int(item[split_at:])
        if item_name in daily_sales:
            daily_sales[item_name] += item_price
        else:
            daily_sales[item_name] = item_price

    for name in daily_sales:
        print(name, daily_sales[name])