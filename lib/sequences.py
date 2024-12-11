#!/usr/bin/env python3

def print_fibonacci(length):
    list_i = []
    for i in range(0, length):
        if i == 0:
            element = 0
        elif i == 1:
            element = 1
        else:
            element = list_i[i-1] + list_i[i-2]
        
        list_i.append(element)
    print(list_i)
