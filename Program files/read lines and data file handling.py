f = open("test.txt", 'r')
print(f.name)
f_contents = f.read()
print(f_contents)
f_contents = f.readlines()
print(f_contents)
f_contents = f.readline()
print(f_contents)
for line in f:
    print(line, end='')
f_contents = f.read(50)
print(f_contents)
size_to_read = 10
f_contents = f.read(size_to_read)
while len(f_contents) > 0:
    print(f_contents)
    print(f.tell())
    f_contents = f.read(size_to_read)
