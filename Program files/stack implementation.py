# Implementation of List as stack
s = []
c = "y"
while (c == "y"):
    print("1. PUSH")
    print("2. POP ")
    print("3. Display")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        a = input("Enter any number :")
        s.append(a)
    elif (choice == 2):
        if (s == []):
            print("Stack Empty")
        else:
            print("Deleted element is : ", s.pop())
    elif (choice == 3):
        l = len(s)
        for i in range(l - 1, -1, -1):  # To display elements from last element to first
            print (s[i])
    else:
        print("Wrong Input")
    c = input("Do you want to continue or not? ")
