# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == "__main__":

    N = int(input()) # number of students
    column_names = input()
    marks = namedtuple("marks", column_names)
    sum_of_marks = 0

    for row_number in range(N):
        raw_data = input().split()
        the_row = marks(raw_data[0], raw_data[1], raw_data[2], raw_data[3])
        sum_of_marks += int(the_row.MARKS)

    print(round(sum_of_marks / N, 2))