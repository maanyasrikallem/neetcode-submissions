class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)

        buckets = [[] for i in range(len(nums)+1)]

        for key in freq :
            buckets[freq[key]].append(key)
        ans = []
        count = 0
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans 
            
        
            
                     
        