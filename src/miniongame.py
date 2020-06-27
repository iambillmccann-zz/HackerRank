def is_vowel(character):
    return True if character.lower() in ['a', 'e', 'i', 'o', 'u'] else False

def count_substrings(string, dict):

    new_string = string
    while new_string != "":
        count = dict[new_string] + 1 if new_string in dict else 1
        dict[new_string] = count
        new_string = new_string[:-1]
    return dict

def sum_dict(dict):

    sum = 0
    for string, count in dict.items():
        sum += count
    return sum

def minion_game(string):
    # your code goes here

    stuart = {}
    kevin = {}
    stuart_count = 0
    kevin_count = 0
    new_string = s.lower()

    while new_string != "":
        character = new_string[0]
        if is_vowel(character):
            kevin = count_substrings(new_string, kevin)
        else:
            stuart = count_substrings(new_string, stuart)

        new_string = new_string[1:]

    stuart_count = sum_dict(stuart)
    kevin_count = sum_dict(kevin)

    if stuart_count > kevin_count:
        print("Stuart {}".format(stuart_count))
    elif kevin_count > stuart_count:
        print("Kevin {}".format(kevin_count))
    else:
        print("Draw")


if __name__ == '__main__':
    file = open("./data/minion-testcase-10.txt", "r")
    s = file.read()
    minion_game(s)