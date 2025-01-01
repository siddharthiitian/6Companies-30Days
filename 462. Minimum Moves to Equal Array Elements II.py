class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if len(nums)%2 != 0 :
            mid_1 = len(nums)//2
            mid_2 = mid_1+1
            mid = min(mid_1,mid_2)
            for i in range(len(nums)):
                ans = ans + abs(nums[i]-nums[mid])
            
            return ans
        
        if len(nums)%2 == 0:
            mid = len(nums)//2
            for i in range(len(nums)):
                ans = ans + abs(nums[i]-nums[mid]) 

            return ans