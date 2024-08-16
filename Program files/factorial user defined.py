#done
#Module factfunc
def fact(no):
    while no > 0:
        f=f*no
        no=no-1
    return f


# Using function
import factfunc
x = int(input("Enter value for factorial : "))
ans = factfunc.fact(x)
print(ans)
