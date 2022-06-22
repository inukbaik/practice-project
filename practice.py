def foo(lst):
    n = len(lst)
    while n > 0:
        tmp = [0] * len(lst)
        new_rng = list(range(len(tmp)))
        print(new_rng[n - 1])
        n //= 3

a = [1, 2, 3, 4]

foo(a)
print(a)