class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[1]>nums[0]:
                return 1
            return 0
        for i in range(1,len(nums)):
            if i==len(nums)-1:
                if nums[len(nums)-1]>nums[len(nums)-2]:
                    return i
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        return 0
