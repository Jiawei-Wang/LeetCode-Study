# follow/unfollow: hashmap (key: user, value: hashset (other users that this user follows))
# post: hashmap (key: user, value: list of counter and tweet id, counter is used as timestamp)
# getFeed: heap 
class Twitter:
    # 初始化3个变量：counter，两个hashmap
    def __init__(self):
        self.count = 0 # counter
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId
         
    # 直接将tweet加入list尾部，并更新counter即可
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # minheap中找出最新的tweet，所以counter要递减

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # 元素顺序从左到右为：tweet的新旧程度，新的（即count更小的）在左边
        minHeap = []
        # 一个corner case，每个用户不follow自己，但默认自己的tweet出现在feed中
        self.followMap[userId].add(userId)
        # 将这个user follow的所有其他user的所有tweet收集起来
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # 找出每个被follow的user发的最后一个tweet并加入heap
                index = len(self.tweetMap[followeeId]) - 1 
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index -1]) # count用于sort heap，tweetId是返回内容，followeeId和index用于记录在tweetMap中的位置
        heapq.heapify(minHeap)
        # 一直搜索直到达到10个，或者已经搜遍全部可用tweet
        while minHeap and len(res) < 10:
            # 每次从heap中取出最新的tweet
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # 然后将这个user的前一条tweet加入heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
            
             
    
    # 直接将id加入set即可
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    # 先检查id是否在set中，再移除
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


# 2024
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # tweetId is not sorted (a newer post can have a smaller tweetId with an older post with a bigger tweetId)
        # so to sort posts we need timestamp
        self.timestamp = 0 

        # key = user, value = set of all users this user follows
        self.relationship = defaultdict(set) 

        # key = user, value = list of all post from this user
        # post: tuple of (timestamp, tweetId), so this list is increasing  
        self.post = defaultdict(list) 

    def follow(self, followerId: int, followeeId: int) -> None:
        # update relationship
        self.relationship[followerId].add(followeeId)
          

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # update relationship
        if followeeId in self.relationship[followerId]:
            self.relationship[followerId].remove(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # if a user posts, we need to add the user as it's own follower
        self.follow(userId, userId)

        # update this user's own post list
        self.timestamp += 1 
        self.post[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_heap = []
        for user in self.relationship[userId]:
            for post in self.post[user][::-1]:
                if len(feed_heap) < 10:
                    heapq.heappush(feed_heap, post)
                else:
                    heapq.heappushpop(feed_heap, post)
        feed = []
        while feed_heap:
            timestamp, tweetId = heapq.heappop(feed_heap)
            feed.append(tweetId)
        return feed[::-1]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)