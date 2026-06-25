class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)

        if endWord not in wordList :
            return 0 

        q = deque([(beginWord,1)])
        visited = set()

        visited.add(beginWord)

        while q :

            word , steps = q.popleft()

            if word == endWord :
                return steps

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz" :

                    if ch == word[i] :
                        continue

                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in wordList and new_word not in visited :

                        q.append((new_word , steps+1))
                        visited.add(new_word)

        return 0

