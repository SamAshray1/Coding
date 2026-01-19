class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fibo = [0,1]

            for i in range(2,n):
                # print(i)
                fibo.append(fibo[i-1]+fibo[i-2])

            return fibo[n-1] + fibo[n-2] 
        