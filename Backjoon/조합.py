n, m = map(int, input().split())


def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod


def npr(n, r):
    assert 0 <= r <= n
    return product(range(n - r + 1, n + 1))


def ncr(n, r):
    assert 0 <= r <= n
    if r > n // 2:
        r = n - r
    return npr(n, r) // factorial(r)


print(ncr(n, m))
