class Twitter:

    def __init__(self):

        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time += 1 

        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        self.following[userId].add(userId)

        for person in self.following[userId] :

            for time , tweet in self.tweets[person] :

                heapq.heappush(heap , (time,tweet))

                if len(heap) > 10 :
                    heapq.heappop(heap)

        heap.sort(reverse=True)

        return [tweet for t, tweet in heap]


    def follow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
