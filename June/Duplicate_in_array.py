In O(1) space complexity and less than O(n^2) runtime 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''y=[0]*(len(nums))
        for x in nums: 
            if y[abs(x)-1]<0: 
                return (abs(x))
            else: 
                y[abs(x)-1]=(-1)*nums[abs(x)-1]'''
        '''x=[]
        for i in nums: 
            if i not in x: 
                x.append(i)
            else: 
                return i
                break'''
        
        # Find the intersection point of the two runners.
        slow = fast = nums[0]
        while True:
            slow= nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
