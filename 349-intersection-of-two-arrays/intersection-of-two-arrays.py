class Solution(object):
    def intersection(self, nums1, nums2):
        seen1=set(nums1)
        seen2=set(nums2)
        res=[]
        for n in seen1:
            if n in seen2:
                res.append(n)
        return res
        