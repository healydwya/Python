class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)-2):
            if nums[i]==nums[i+2]:
                nums.remove(nums[i])
                i-=1
            i+=1
        return len(nums)
        