#done
#Floyd's triangle
n=int(input("Enter the number :"))
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print (j,end=' ')
    print('\n')


