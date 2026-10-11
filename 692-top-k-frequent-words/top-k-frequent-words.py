class Solution(object):
    def topKFrequent(self, words, k):
        count=Counter(words)
        res=[]
        for i ,freq in count.most_common():
            res.append(i)
        res.sort(key=lambda word:(-count[word],word))
        return res[:k]
        