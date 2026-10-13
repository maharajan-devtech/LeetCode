class Solution(object):
    def threeSum(self, nums):
        target=0
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==target:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    
                elif total<target:
                    j+=1
                else:
                    k-=1
        return ans

        