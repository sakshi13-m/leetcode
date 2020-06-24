unique binary search tree 
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=dp[1] = 1
        for i in range(2,n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
                print(dp)
        return dp[n]
        '''res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
    # Catalan Number  (2n)!/((n+1)!*n!) 
    def numTrees(self, n):
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))'''
