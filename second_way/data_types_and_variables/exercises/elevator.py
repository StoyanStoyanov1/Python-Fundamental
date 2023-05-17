from math import ceil

persons = int(input())
capacity = int(input())

courses = persons / capacity

print(ceil(courses))
