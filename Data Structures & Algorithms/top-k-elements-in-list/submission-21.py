class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     nums=list(Counter(nums).items())
    #     nums.sort(key= lambda x:x[1], reverse=True)
    #     ans=[]
    #     for i in range(k):
    #         ans.append(nums[i][0])
    #     return ans
    
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     nums=Counter(nums)
    #     temp=defaultdict(list)
    #     for i in nums:
    #         temp[nums[i]].append(i)
    #     nums=[-i for i in temp.keys()]
    #     heapq.heapify(nums)
    #     ans=[]
    #     while(len(ans)<k):
    #         ans.extend(temp[-nums[0]])
    #         heapq.heappop(nums)
    #     return ans

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_b=len(nums)
        nums=Counter(nums)
        buckets=[[] for _ in range(n_b)]
        for i in nums:
            buckets[nums[i]-1].append(i)
        final=[]
        for i in range(len(buckets)-1,-1,-1):
            final.extend(buckets[i])
            if(len(final)==k):
                return final


            


        