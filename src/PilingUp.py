# Enter your code here. Read input from STDIN. Print output to STDOUT

def run_test_case(cubes):

    basecube = 2 ** 31
    counter = 0
    max_index = len(cubes) - 1
    min_index = 0

    while True:
        index = min_index if cubes[min_index] > cubes[max_index] else max_index
        if cubes[index] > basecube : return "No"
        if min_index >= max_index : return "Yes"
        basecube = cubes[index]
        min_index = min_index + 1 if min_index == index else min_index
        max_index = max_index - 1 if max_index == index else max_index
        counter += 1
        if counter > 100000 : break

        

if __name__ == "__main__":
    T = int(input())      # This is the number of test cases
    for index in range(T):
        n = int(input())  # The number of cubes
        print(run_test_case(list(map(int, input().split()))))
