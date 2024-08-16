arr = []
def array_operation():
    ch = 1
    while ch != 10:
        print('Various Array operation\n')
        print('1 Create and Enter value\n')
        print('2 Print Array\n')
        print('3 Reverse Array\n')
        print('4 Linear Search\n')
        print('5 Binary Search\n')
        print('6 Lowest Number \n')
        print('7 Selection Sort\n')
        print('10 Exit\n')
        ch = int(input('Enter Choice '))
        if ch == 1:
            appendarray()
        elif ch == 2:
            print_array()
        elif ch == 3:
            reverse_array()
        elif ch == 4:
            linear_search()
        elif ch == 5:
            binary_search()
        elif ch == 6:
            min_number()
        elif ch == 7:
            selection_sort()
def appendarray():
    for i in range(0, 10):
        x = int(input('Enter Number : '))
        arr.insert(i, x)
# ----------------------------------------------------------------------------------------------------------------------

def print_array():
    for i in range(0, 10):
        print(arr[i]),

# -------------------------------------------------------------------------------------------------------------------------
def reverse_array():
    for i in range(1, 11):
        print(arr[-i]),
# -------------------------------------------------------------------------------------------------------------------------
def lsearch():
    try:
        x = int(input('Enter the Number You want to search : '))
        n = arr.index(x)
        print('Number Found at %d location'%(n + 1))
    except:
        print('Number Not Exist in list')
# ------------------------------------------------------------------------------------------------------------------------
def linear_search():
    x = int(input('Enter the Number you want to search : '))
    fl = 0
    for i in range(0, 10):
        if arr[i] == x:
            fl = 1
            print('Number Found at %d location' % (i + 1))
            break
    if fl == 0:
        print('Number Not Found')
# -------------------------------------------------------------------------------------------------------------------------
def binary_search():
    x = int(input('Enter the Number you want to search : '))
    fl = 0
    low = 0
    heigh = len(arr)
    while low <= heigh:
        mid = int((low + heigh)//2)
        if arr[mid] == x:
            fl = 1
            print('Number Found at %d location' % (mid + 1))
            break
        elif arr[mid] > x:
            low = mid + 1
        else:
            heigh = mid - 1
    if fl == 0:
        print('Number Not Found')
# ----------------------------------------------------------------------------------------------------------------------

def min_number():
    n = arr[0]
    k = 0
    for i in range(0, 10):
        if arr[i] < n:
            n = arr[i]
            k = i
    print('The Lowest number is %d ' % (n))
# ---------------------------------------------------------------------------------------------------------------------

def selection_sort():
    for i in range(0, 10):
        n = arr[i]
        k = i
        for j in range(i + 1, 10):
            if arr[j] < n:
                n = arr[j]
                k = j
                arr[k] = arr[i]
                arr[i] = n
array_operation()
