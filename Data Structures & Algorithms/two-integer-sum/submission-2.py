class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        ind=defaultdict(list)
        for i in range(len(nums)):
            ind[nums[i]].append(i)
        s= set(ind.keys())
        for i in ind.keys():
            if(target-i in s):
                tupl= (ind[i][0], ind[target-i][-1])
                if(tupl[0]!=tupl[1]):
                    return([min(tupl), max(tupl)])
        