class TimeMap:

    def __init__(self):

        self.names = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.names[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:

        arr = self.names[key]

        left = 0
        right = len(arr) - 1

        ans = ""

        while left <= right :

            mid = (left+right) //2 

            if arr[mid][1] <= timestamp :
                ans = arr[mid][0]
                left = mid +1

            else:
                right = mid - 1

        return ans 


