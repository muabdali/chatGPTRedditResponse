from chatgpt_wrapper import ChatGPT


class bot_call():
    def __init__(self, comment):
        global response
        bot_call.bot = ChatGPT()
        bot_call.response = bot_call.bot.ask(f"Give me a witty reply to this reddit comment: '{comment}'. Please keep it one to two sentences long.")
        response = bot_call.response
        print(response)


# make reddit api search for comments in specific subreddits
# MAKE SURE TO REMOVE REDDIT ACCESS KEYS WHEN INCORPARATING IT


TEST = bot_call("Manchester United is a bigger club than Manchester City")

# set limit of witty comments to two per reddit thread
# focus on subreddits such as ShowerThoughts, Soccer etc.

# experiment will be of two parts, one focusing on short comments (such as r/showerthoughts) and others focusing on long paragraphs (such as r/subredditdrama). 
# i hypothesize that the longer statement replys will be better because the bot will have more context