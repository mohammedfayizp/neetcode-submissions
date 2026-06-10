class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=list(Counter(nums).items())
        nums.sort(key= lambda x:x[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(nums[i][0])
        return ans

        