# brings all tokens, client id etc into file
from redditTokenInit import *
import praw

reddit = praw.Reddit(
    client_id = client_id,
    client_secret  = client_secret,
    password = account_password,
    user_agent = "TEST by u/DingDingPowow",
    username = account_name
)

with open('subredditlist.txt', 'r') as file:
    contents = file.readlines()


for subredditName in contents:
    print(f'r/{subredditName}')
    
