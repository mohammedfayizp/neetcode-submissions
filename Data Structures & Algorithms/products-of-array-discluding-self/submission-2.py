class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]
        suf=[1]

        for i in range(len(nums)-1):
            pref.append(pref[-1]*nums[i])
        nums.reverse()
        for i in range(len(nums)-1):
            suf.append(suf[-1]*nums[i])
        suf.reverse()
        final=[]
        for i in range(len(nums)):
            final.append(pref[i]*suf[i])
        return final
        