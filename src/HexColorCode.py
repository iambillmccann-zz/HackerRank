# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    N = int(input())
    regex = r"(?i)#(?:[0-9a-f]{6}|[0-9a-f]{3})(?=[;,)])"

    for index in range(N):
        css_data = input()
        matches = re.findall(regex, css_data)
        for color_code in matches:
            print(color_code)
