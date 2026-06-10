class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            target=-nums[i]
            left, right=i+1, len(nums)-1
            while(left<right):
                total=nums[left]+nums[right]
                if(total==target):
                    first=min([-target, nums[left], nums[right]])
                    second=max([-target, nums[left], nums[right]])
                    third= -(first+second)
                    result.append((first, second, third))
                    left+=1
                    right-=1
                if(total<target):
                    left+=1
                if(total>target):
                    right-=1
        result=list(set(result))
        result=[list(i) for i in result]
        return result
                