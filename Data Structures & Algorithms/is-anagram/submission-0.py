class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = Counter(s)
        freq_2 = Counter(t)

        return freq_1 == freq_2
        