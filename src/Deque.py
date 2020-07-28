# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == "__main__":
    N = int(input())    # number of operations
    the_list = deque([])

    for index in range(N):
        command_line = input().split()
        operation = command_line[0]

        if operation.lower() == 'append': the_list.append(command_line[1])
        elif operation.lower() == 'appendleft' : the_list.appendleft(command_line[1])
        elif operation.lower() == 'pop' : the_list.pop()
        elif operation.lower() == 'popleft' : the_list.popleft()
        else : print("Invalid Command")

    print(*the_list)
