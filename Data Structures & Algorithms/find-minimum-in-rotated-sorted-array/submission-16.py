class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right= 0, len(nums)-1
        if(nums[left]<=nums[right]):
            return nums[left]
        while(right-left+1>2):
            mid=left+(right-left+1)//2
            if(nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
                return nums[mid]
            elif(nums[mid]>nums[left] and nums[mid]>nums[right]):
                left=mid
            elif(nums[mid]<nums[right] and nums[mid]<nums[left]):
                right=mid
        return min(nums[left], nums[right])
