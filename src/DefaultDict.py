# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    
    values = input().split(' ')
    n = int(values[0])
    m = int(values[1])

    A = defaultdict(list)
    for index in range(1, n + 1):
        word = input()
        A[word].append(index)

    for index in range(0,m):
        the_list = A[input()]
        if len(the_list) == 0:
            print("-1")
            continue

        for item in the_list:
            print("{} ".format(item),end="")
        print("")