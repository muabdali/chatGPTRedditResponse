from praw import reddit as praw 




"""
SAMPLE FOR ONE POST, EXTRACTS THE COMMENTS STARTING FROM THE TOP,  NOT REPLIES


# needs submission number from comment link
submission = reddit.submission("3g1jfi")

# takes highest comment
for top_level_comment in submission.comments:
    print(top_level_comment.body)
"""