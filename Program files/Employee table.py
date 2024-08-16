import matplotlib.pyplot as plt
marks=[]
i=0
subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry"]
while i<5:
    marks.append(int(input("Enter Mark = ")))
    i+=1
for j in range(len(marks)):
    print("{}.{} Mark = {}".format(j+1, subjects[j],marks[j]))

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.pie (marks, labels = subjects, autopct = "%1.2f%%")
plt.axes().set_aspect ("equal")
plt.show()
