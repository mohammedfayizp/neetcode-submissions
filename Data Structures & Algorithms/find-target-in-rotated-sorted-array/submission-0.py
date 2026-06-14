class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        while(right-left+1>2):
            mid=left+(right-left+1)//2
            if(target==nums[mid]):
                return mid
            else:
                if(nums[mid]>nums[left]):
                    if(target<nums[mid] and target>=nums[left]):
                        right=mid
                        continue
                    left=mid
                if(nums[mid]<nums[right]):
                    if(target>nums[mid] and target<=nums[right]):
                        left=mid
                        continue
                    right=mid
        if(target ==nums[left]):
            return left
        elif(target==nums[right]):
            return right
        else:
            return -1
                
        