#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python program to print
# duplicates from a list


def repeat(array):
    _size = len(array)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if array[i] == array[j] and array[i] not in repeated:
                repeated.append(array[i])
    return repeated


# Driver Code
# list = ['MSA004','AAI002','NRA010','CBA026']
# print repeat(list)