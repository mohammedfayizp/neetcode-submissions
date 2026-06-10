class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i,val in enumerate(nums):
            if(target-val in seen):
                tupl=(seen[target-val],i)
                return [min(tupl),max(tupl)]
            seen[val]=i
        