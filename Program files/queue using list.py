
# Implementing List as a Queue - using function append() and pop()
a = []
c = 'y'
while (c == 'y'):
    print("1. INSERT")
    print("2. DELETE ")
    print("3. Display")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        b = int(input("Enter new number: "))
        a.append(b)
    elif (choice == 2):
        if (a == []):
            print("Queue Empty")
        else:
            print("Deleted element is:", a[0])
            a.pop(0)
    elif (choice == 3):
        l = len(a)
        for i in range(0, l):
            print(a[i])
    else:
        print("wrong input")
    c = input("Do you want to continue or not: ")

