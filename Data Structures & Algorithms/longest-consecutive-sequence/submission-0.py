class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check=set(nums)
        start=[]
        for i in nums:
            if (i-1 not in check):
                start.append(i)
        ml=0
        for i in start:
            k=i
            temp=1
            while(k+1 in check):
                temp+=1
                k+=1
            ml=max(ml,temp)
        return ml
        