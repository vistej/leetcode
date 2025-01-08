class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.tid = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.tid, tweetId])
        self.tid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        users = self.users[userId]
        users.add(userId)
        feed = []
        for user in users:
            x = len(self.tweets[user])
            tweets = self.tweets[user] if x <= 10 else self.tweets[user][x-10:]
            feed += tweets
        
        heapq.heapify(feed)
        for _ in range(10):
            if feed:
                res.append(heapq.heappop(feed)[1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)