from map_reduce import *


def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return list(set(primfac))


class MapReduceDivisors(MapReduceBase):
    def map_function(self, x):
        for p in primes(x):
            self.emit(p, x)

mr = MapReduceDivisors()
print mr.run([15, 21, 24, 30, 49])

