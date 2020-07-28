# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())  # number of words
    words = OrderedDict()

    for index in range(n):
        word = input().strip()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print(len(words))
    print(*words)