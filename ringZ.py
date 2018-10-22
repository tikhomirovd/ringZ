class Zn(object):

    def __init__(self, n):
        self.n = n

    def modZ(self, x):
        return x % self.n

    def sumZ(self, x, y):
        return self.modZ(x + y)

    def subZ(self, x, y):
        return self.modZ(x - y)

    def multZ(self, x, y):
        return self.modZ(x * y)

    def search_inverse(self, x, n=None, s=1, t=0, N=0):
        if n is None: n = self.n
        MMI = lambda x, n, s=1, t=0, N=0: (n < 2 and t % N or MMI(n, x % n, t, s - x // n * t, N or n), -1)[n < 1]
        return MMI(n, x % n, t, s - x // n * t, N or n)

    def divZ(self, x, y):
        if self.search_inverse(y) != -1:
            return self.modZ(x * self.search_inverse(y))
        else:
            return -1
