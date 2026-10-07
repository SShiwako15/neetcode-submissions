class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        minHeap = []
        self.followMap[userId].add(userId)

        if len(self.followMap[userId]) > 10:
            maxHeap = []

            for follow in self.followMap[userId]:
                if follow in self.tweetMap:
                    index = len(self.tweetMap[follow]) - 1
                    count, tweetId = self.tweetMap[follow][index]
                    heapq.heappush(maxHeap, [-count, tweetId, follow, index - 1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, follow, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, follow, index])
        else:

            for follow in self.followMap[userId]:
                if follow in self.tweetMap:
                    index = len(self.tweetMap[follow]) - 1
                    count, tweetId = self.tweetMap[follow][index]
                    heapq.heappush(minHeap, [count,tweetId, follow, index - 1])

        while minHeap and len(output) < 10:
            count,tweetId, follow, index = heapq.heappop(minHeap)
            output.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[follow][index]
                heapq.heappush(minHeap, [count,tweetId, follow, index - 1])
        
        return output



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
