class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     nums=list(Counter(nums).items())
    #     nums.sort(key= lambda x:x[1], reverse=True)
    #     ans=[]
    #     for i in range(k):
    #         ans.append(nums[i][0])
    #     return ans
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=Counter(nums)
        temp=defaultdict(list)
        for i in nums:
            temp[nums[i]].append(i)
        nums=[-i for i in temp.keys()]
        heapq.heapify(nums)
        ans=[]
        while(len(ans)<k):
            ans.extend(temp[-nums[0]])
            heapq.heappop(nums)
        return ans


        