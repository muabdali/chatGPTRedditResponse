from praw import reddit as praw 
import re


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)


# needs submission number from comment link
submission = reddit.submission("3g1jfi")

# takes highest comment
for top_level_comment in submission.comments:
    print(top_level_comment.body)
