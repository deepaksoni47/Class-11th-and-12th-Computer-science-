#Program to read data from data file in read mode and #append the words starting with letter ‘T’
#in a given file in python
f=open("test.txt",'r')
read=f.readlines()
f.close()
id=[]
for ln in read:
    if ln.startswith("T"):
        id.append(ln)
print(id)
