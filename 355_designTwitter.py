from collections import defaultdict
class Twitter:
    '''
      following: userid -> hashset of userId {
        u1: {u2, u3, u4}
      }

      tweets: userid -> listof tweetsid {
        u1: [tw1, tw2, tw3]
      }

      getNewsFeed: get the first 10 tweets of each user and sort it (nlogn) 

    '''
    def __init__(self):
      self.following = defaultdict(set)
      self.tweets = defaultdict(list)
      self.ts = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
      self.tweets[userId].append((self.ts, tweetId))
      self.ts += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
      "Get 10 recent tweets"
      ls = self.tweets[userId][::-1]
      for user in self.following[userId]:
        ls.extend(self.tweets[user][:-11:-1])
      
      ls = sorted(ls, reverse=True)
      return [tw[1] for tw in ls[:10]] 

        

    def follow(self, followerId: int, followeeId: int) -> None:
      self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
      if followeeId in self.following[followerId]:
        self.following[followerId].remove(followeeId)