
#1

#2
'''

import random

N = 20
n = 0
even = 0
odd = 0

lst = [random.randint(1,10) for i in range(N)]


def get_elements():
    for  j in range(N):
        global n
        global even
        global odd
        if lst[n] % 2 == 0:
            even += 1
        else:
            odd += 1


even_pairs = even // 2
odd_pairs = odd // 2

pairs = even_pairs + odd_pairs

'''

#3
'''
import random

N = 20

lst1 = [random.randint(1,10) for i in range(N)]
lst2 = [random.randint(1,10) for j in range(N)]


sorted_1 = lst1.sort()
sorted_2 = lst2.sort()

a = lst1 + lst2


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):

        swapped = False
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True

        if (swapped==False):
            break
        swapped = False

        end = end-1

        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        start = start + 1


cocktailSort(a)
for i in range(len(a)):
    print("% d" % a[i])
'''


#4
'''
import time


def LinearSearch(lys, element):
    time_start = time.process_time()
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
    time_end = time.process_time()
    print(f'Время {time_end - time_start}')


def BinarySearch(lys, val):
    time_start = time.process_time()
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
    time_end = time.process_time()
    print(f'Время {time_end - time_start}')
'''