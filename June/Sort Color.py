hsis

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums=nums.sort()
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        x=0
        
        for i in sorted(d):
            for y in range(d[i]):
                nums[x]=i
                x+=1
        
