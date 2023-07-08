import numpy 

n,m = map(int, input().split())

L1 = numpy.array(list(map(int, input().split())))
L2 = numpy.array(list(map(int, input().split())))

print(numpy.add(L1, L2))
print(numpy.subtract(L1,L2))
print(numpy.multiply(L1,L2))
print(numpy.floor_divide(L1,L2))
print(numpy.mod(L1,L2))
print(numpy.power(L1,L2))