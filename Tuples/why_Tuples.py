import timeit

print("List =",timeit.timeit(stmt="['An','ki','t',21,24,67]",number=193334475))
print("Tuples=",timeit.timeit(stmt="('An','ki','t',21,24,67)",number=193334475))
