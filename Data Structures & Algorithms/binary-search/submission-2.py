class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = 0
        for i in range(len(nums)):
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            if target>nums[mid]:
                start = mid+1
            if target<nums[mid]:
                end = mid-1
        
        return -1