class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [-self.timer, tweetId]
        self.tweets[userId].append(tweet)    
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        allUsers = self.users[userId]
        allUsers.add(userId)

        heap = []
        
        for user in allUsers:
            if self.tweets[user]:
                timer, latest_tweet = self.tweets[user][-1]
            else:
                continue
            idx = len(self.tweets[user]) - 1
            heapq.heappush(heap, [timer, user, latest_tweet, idx - 1])
        
        feed = []
        
        while heap and len(feed) < 10:
            timer, user, tweet, idx = heapq.heappop(heap)
            if idx >= 0:
                new_timer, new_tweet = self.tweets[user][idx]    
                heapq.heappush(heap, [new_timer, user, new_tweet, idx-1])
            feed.append(tweet)
        
        return feed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
