class Solution(object):
    lister=[0,1]
    def fib(self, n):
        if n<len(self.lister):
            return self.lister[n]
        else:
            self.lister.append(self.fib(n-1)+self.fib(n-2))
            return self.lister[n]
