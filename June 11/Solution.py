class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-i):
                if j+1<len(nums)-i:
                    if nums[j+1]<nums[j]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
            
        return nums