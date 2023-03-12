from redditTokenInit import *
import praw

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=account_password,
    user_agent="TEST by u/DingDingPowow",
    username=account_name
)


class postGrabber:
    def __init__(self, subredditlist):
        self.subredditlist = subredditlist
        self.subreddits = self.subredditlist_init()

    def subredditlist_init(self):
        with open(self.subredditlist, 'r') as file:
            contents = file.readlines()
        subreddits = []
        for subredditName in contents:
            subreddit = reddit.subreddit(subredditName.strip())
            subreddits.append(subreddit)
            print(f'r/{subredditName.strip()}')
        return subreddits


run = postGrabber('subredditlist.txt')
targetList = run.subreddits
print(targetList.strip())