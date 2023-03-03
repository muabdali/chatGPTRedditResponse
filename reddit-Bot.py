from praw import reddit as praw 


with open('test.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()


for line in contents:
    # Check if the line contains "client_id"
    if "client_id" in line:
        # Split the line on the = character
        parts = line.split('=')
        # Get the second part (the value) and remove any whitespace
        client_id = parts[1].strip()

    # Check if the line contains "client_code"
    elif "client_code" in line:
        # Split the line on the = character
        parts = line.split('=')
        # Get the second part (the value) and remove any whitespace
        client_code = parts[1].strip()

# Print the results
print(client_id)
print(client_code)



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
