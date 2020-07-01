# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    x = input()
    shoes = input()
    shoes = list(map(int, shoes.split(' ')))
    n = input()
    sales = 0

    inventory = Counter(shoes)

    for iteratior in range(0,int(n)):
        customer_data = input()
        size, price = customer_data.split(' ')
        size = int(size)
        price = int(price)

        if size in inventory:
            if inventory[size] > 0:
                sales += price
                inventory[size] -= 1

    print(sales)