def minion_game(string):
    # your code goes here

    stuart_count = 0
    kevin_count = 0
    position = 0
    substrings = len(string)

    while substrings > 0:

        if string[position] in ['A', 'E', 'I', 'O', 'U']:
            kevin_count += substrings
        else:
            stuart_count += substrings

        position += 1
        substrings -= 1

    if stuart_count > kevin_count:
        print("Stuart {}".format(stuart_count))
    elif kevin_count > stuart_count:
        print("Kevin {}".format(kevin_count))
    else:
        print("Draw")

if __name__ == '__main__':
    file = open("./data/minion-testcase-13.txt", "r")
    s = file.read()

    minion_game(s)