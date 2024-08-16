#done
# Program to enter the string and check if it’s palindrome or not using ‘for’ loop.
msg = input("Enter any string : ")
newlist = []
newlist[:0] = msg
l = len(newlist)
ed = l - 1
for i in range(0, l):
    if newlist[i] != newlist[ed]:
        print("Given String is not a palindrome")
        break
    if i >= ed:
        print("Given String is a palindrome")
        break
    l = l - 1
    ed = ed - 1

