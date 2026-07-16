class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = 0
        for _ in range(len(nums)):
            mid = (start+end)//2
            if start>end:
                break
            elif target == nums[mid]:
                return mid
            elif target>nums[mid]:
                start = mid+1
            else:
                target<nums[mid]
                end = mid-1
        
        return -1