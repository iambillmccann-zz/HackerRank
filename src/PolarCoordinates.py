# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import cmath

def parse_complex_number(string):

    complex_number = string.strip()
    x_is_negative = True if complex_number[0] == '-' else False
    complex_number = complex_number[1:] if x_is_negative else complex_number
    y_is_negative = True if '-' in complex_number else False
    parts = complex_number.split('-') if y_is_negative else complex_number.split('+')
    x = int(parts[0]) * -1 if x_is_negative else int(parts[0])
    y = int(parts[1][:-1]) * -1 if y_is_negative else int(parts[1][:-1])
    return (x, y)


if __name__ == '__main__':

    my_input = '-1-5j' # input()

    x, y = parse_complex_number(my_input)

    r = math.sqrt( (x*x) + (y*y) )
    theta = cmath.phase(complex(x,y))
    print(r)
    print(theta)