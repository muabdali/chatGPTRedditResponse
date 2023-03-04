from praw import reddit as praw 


with open('redditTokens.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()


for line in contents:
    # Check if the line contains "client_id"
    if "client_id" in line:
        # Split the line on the = character
        parts = line.split('=')
        # Get the second part (the value) and remove any whitespace
        client_idfromTXT = parts[1].strip()

    # Check if the line contains "client_code"
    elif "client_secret" in line:
        # Split the line on the = character
        parts = line.split('=')
        # Get the second part (the value) and remove any whitespace
        client_code = parts[1].strip()
        print(client_code)
    elif "account_password" in line:
        parts = line.split('=')
        password_part = parts[1].strip()


# Print the results
print(client_idfromTXT)
print(client_code)



reddit = praw.Reddit(
    client_id=client_idfromTXT,
    client_secret=client_code,
    password=password_part,
    user_agent="",
    username="",
)


# needs submission number from comment link
submission = reddit.submission("3g1jfi")

# takes highest comment
for top_level_comment in submission.comments:
    print(top_level_comment.body)
