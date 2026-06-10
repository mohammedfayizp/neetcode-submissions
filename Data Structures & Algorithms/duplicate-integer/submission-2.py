class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        count=Counter(nums)
        a=list(count.values())
        for i in a:
            if(i>=2):
                return True
        return False
        