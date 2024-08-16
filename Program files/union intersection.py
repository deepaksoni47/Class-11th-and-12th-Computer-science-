#done
odd=set([x*1+2 for x in range(0,5)])
primes=set()
for i in range(2,10):
    j=2
    f=0
    while j<i/2:
        if i%j == 0:
            f=1
        j+=1
    if f==0:
        primes.add(i)
print("Odd Numbers: ", odd)
print("Prime Numbers: ", primes)
print("Union: ", odd.union(primes))
print("Intersection: ", odd.intersection(primes))
print("Difference: ", odd.difference(primes))
print("Symmetric Difference: ", odd.symmetric_difference(primes))


