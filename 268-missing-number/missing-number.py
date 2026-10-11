class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        seen=set(nums)
        for i in range(n+1):
            if i not in seen:
                return i



        