# Program to read data from data file in read mode and
# count the particular word occurrences in given string,
# number of times in python.
f = open("test.txt", 'r')
read = f.readlines()
f.close()
times = 0  # the variable has been created to show the number of times the loop runs
times2=0 #the variable has been created to show the number of times the loop runs
chk=input("Enter String to search : ")
count = 0
for sentence in read:
    line = sentence.split()
    times += 1
    for each in line:
        line2 = each
        times2 += 1
        if chk == line2:
            count += 1
print("The search String ", chk, "is present : ", count, "times")
print(times)
print(times2)
