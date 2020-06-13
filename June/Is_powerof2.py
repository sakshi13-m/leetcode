python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n>=1):
            x=bin(n).count('1')
            if(x==1): 
                return True
            else:
                return False
        else:
            return False
