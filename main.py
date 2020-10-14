import time


def merge_sort(my_list, left, right):
    if right - left > 1:
        middle = (left + right) // 2
        merge_sort(my_list, left, middle)
        merge_sort(my_list, middle, right)
        merge_list(my_list, left, middle, right)


def merge_list(my_list, left, middle, right):
    left_list = my_list[left:middle]
    right_list = my_list[middle:right]
    k = left
    i = 0
    j = 0
    while left + i < middle and middle + j < right:
        if left_list[i] <= right_list[j]:
            my_list[k] = left_list[i]
            i = i + 1
        else:
            my_list[k] = right_list[j]
            j = j + 1
        k = k + 1
    if left + i < middle:
        while k < right:
            my_list[k] = left_list[i]
            i = i + 1
            k = k + 1
    else:
        while k < right:
            my_list[k] = right_list[j]
            j = j + 1
            k = k + 1


def bubble_sort(my_list):  # a = name of list
    b = len(my_list) - 1
    for x in range(b):
        for y in range(b - x):
            if my_list[y] > my_list[y + 1]:
                my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
    return my_list


def insertion_sort(my_list):
    for x in range(1, len(my_list)):
        k = my_list[x]  # element present at index number 1
        j = x - 1
        while j >= 0 and k < my_list[j]:  # comparing elements with the next until the last item
            my_list[j + 1] = my_list[j]
            j -= 1  # comparing each element to the elements present to its left
        my_list[j + 1] = k  # new item becomes the key


def selection_sort(my_list, r):
    for x in range(r):
        minimum = x  # first element is assumed to be the minimum
        for y in range(x + 1, r):
            if my_list[y] < my_list[minimum]:  # comparing minimum with the next element
                minimum = y
        (my_list[x], my_list[minimum]) = (my_list[minimum], my_list[x])  # swap elements if required


def shell_sort(my_list, n):
    g = n // 2  # dividing the number of elements by 2 to find the gap
    while g > 0:
        for x in range(g, n):
            y = my_list[x]
            z = x
            while z >= g and my_list[z - g] > y:
                my_list[z] = my_list[z - g]
                z -= g
            my_list[z] = y
        g //= 2


print()
print("This program demonstrates the speed of different sorting algorithms")
print("The algorithms will sort a .txt file with 10,000 integers")
print("(May take several seconds to load)")
print()

# Resets the list "data" from file
with open('Random.txt', 'r') as f:
    next(f)
    data = list(map(int, f))

start = time.process_time()
merge_sort(data, 0, len(data))
print("Merge sort:", time.process_time() - start)

# Resets the list "data" from file
with open('Random.txt', 'r') as f:
    next(f)
    data = list(map(int, f))

start = time.process_time()
bubble_sort(data)
print("Bubble sort:", time.process_time() - start)

# Resets the list "data" from file
with open('Random.txt', 'r') as f:
    next(f)
    data = list(map(int, f))

start = time.process_time()
insertion_sort(data)
print("Insertion sort:", time.process_time() - start)

# Resets the list "data" from file
with open('Random.txt', 'r') as f:
    next(f)
    data = list(map(int, f))

start = time.process_time()
selection_sort(data, len(data))
print("Selection sort:", time.process_time() - start)

# Resets the list "data" from file
with open('Random.txt', 'r') as f:
    next(f)
    data = list(map(int, f))

start = time.process_time()
shell_sort(data, len(data))
print("Shell sort:", time.process_time() - start)
