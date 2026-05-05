import timeit
print("Lists: ",timeit.timeit(
    stmt="['Ankit']",
    number=300000099
))
print("Tuple: ",timeit.timeit(
    stmt="('Ankit')",
    number=300000099
))