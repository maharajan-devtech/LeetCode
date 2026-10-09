class Solution(object):
    def topKFrequent(self, nums, k):
        count=Counter(nums)
        res=[]
        for num ,freq in count.most_common(k):
            res.append(num)
        return res
        