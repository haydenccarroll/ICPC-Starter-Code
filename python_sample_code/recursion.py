def recursive_sum(n):
    if n == 0:
        return 0
    return recursive_sum(n-1) + n

print(recursive_sum(3))
# (0 + 1 + 2 + 3)