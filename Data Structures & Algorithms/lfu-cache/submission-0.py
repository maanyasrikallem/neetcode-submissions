from collections import defaultdict


class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1

        self.prev = None
        self.next = None


class DLL:

    def __init__(self):

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self, node):

        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

        self.size += 1

    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def pop_last(self):

        if self.size == 0:
            return None

        node = self.tail.prev

        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.curr_size = 0

        self.key_to_node = {}

        self.freq_to_list = defaultdict(DLL)

        self.min_freq = 0

    def update_freq(self, node):

        freq = node.freq

        self.freq_to_list[freq].remove(node)

        if freq == self.min_freq and self.freq_to_list[freq].size == 0:
            self.min_freq += 1

        node.freq += 1

        self.freq_to_list[node.freq].add(node)

    def get(self, key: int) -> int:

        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        self.update_freq(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.key_to_node:

            node = self.key_to_node[key]

            node.value = value

            self.update_freq(node)

            return

        if self.curr_size == self.capacity:

            node = self.freq_to_list[self.min_freq].pop_last()

            del self.key_to_node[node.key]

            self.curr_size -= 1

        node = Node(key, value)

        self.key_to_node[key] = node

        self.freq_to_list[1].add(node)

        self.min_freq = 1

        self.curr_size += 1