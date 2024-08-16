#done
#	To find whether a number is perfect or not
def pernum(num):
    divsum=0
    for i in range(1,num):
        if num%i == 0:
            divsum+=i
    if divsum==num:
        print('Perfect Number')
    else:
        print('Not a perfect number')
pernum(6)
pernum(15)

