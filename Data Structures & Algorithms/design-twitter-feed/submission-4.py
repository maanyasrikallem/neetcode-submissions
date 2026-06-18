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

            if self.tweets[person] :

                idx = len(self.tweets[person]) - 1 

                time , tweet = self.tweets[person][idx]

                heapq.heappush(heap , (-time , tweet , person , idx))

        res = []

        while heap and len(res) < 10 :

            neg_time , tweet , person , idx = heapq.heappop(heap)

            res.append(tweet)

            if idx > 0 :

                time , tweet = self.tweets[person][idx-1]

                heapq.heappush(heap , (-time , tweet , person , idx-1))

        return res



    def follow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
