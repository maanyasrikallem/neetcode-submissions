from collections import defaultdict

class FreqStack:

    def __init__(self):

        self.freq = {}
        self.groups = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:

        self.freq[val] = self.freq.get(val, 0) + 1

        self.groups[self.freq[val]].append(val)

        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:

        val = self.groups[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.groups[self.max_freq]:
            self.max_freq -= 1

        return val