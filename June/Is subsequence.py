class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        it=iter(s)
        for i in t:
            if i not in it:
                #print(t)
                return False 
            
        '''i=0
        j=0
        while(i<len(s) and j<len(t)):
            y=s.index(t[j])
            if(y>i):
                i=y
                print(i,t[j])
            else: 
                print(i,t[j])
                return False
            j+=1'''
            
            
        return True
        
