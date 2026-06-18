class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for word in strs :
            freq = [0]*26

            for i in word:
                freq[ord(i) - ord('a')] += 1
            
            answer[tuple(freq)].append(word) 

        return list(answer.values())


        