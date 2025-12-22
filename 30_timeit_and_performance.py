print('Performance and Timeit module')
# Experiment with sieve of Eratosthenes
print([x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1])
