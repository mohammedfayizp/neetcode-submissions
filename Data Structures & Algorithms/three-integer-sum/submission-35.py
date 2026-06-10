class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        prev=set([None, None, None])
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            val=nums[i]
            curr =[i+1,-1]
            p1=nums[i+1]
            p2=nums[-1]
            if(val+p1+p2==0):
                if(set([val, p1, p2])!=prev):
                    result.append([val, p1, p2])
                prev=set([val, p1, p2])
            while(-curr[1]<len(nums)-i and curr[0]<len(nums)-1 and curr[0]<len(nums)+curr[1]):
                if(val+p1+p2>=0):
                    curr[1]-=1
                    p2=nums[curr[1]]
                    if(val+p1+p2==0 and curr[0]<len(nums)+curr[1]):
                        if(set([val, p1, p2])!=prev):
                            result.append([val, p1, p2])
                        prev=set([val, p1, p2])
                if(val+p1+p2<=0 and curr[0]<len(nums)-1):
                    curr[0]+=1
                p1=nums[curr[0]]
                if(val+p1+p2==0 and curr[0]<len(nums)+curr[1]):
                    if(set([val, p1, p2])!=prev):
                        result.append([val, p1, p2])
                    prev=set([val, p1, p2])

                
        return result
            
            




        