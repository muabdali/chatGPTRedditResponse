class RedditTokens:
    def __init__(self, filename):
        self.client_id = ''
        self.client_secret = ''
        self.account_password = ''
        self.account_name = ''
        self.read_tokens(filename)

    def read_tokens(self, filename):
        with open(filename, 'r') as file:
            contents = file.readlines()

        for line in contents:
            if "client_id" in line:
                parts = line.split('=')
                self.client_id = parts[1].strip()

            elif "client_secret" in line:
                parts = line.split('=')
                self.client_secret = parts[1].strip()

            elif "account_password" in line:
                parts = line.split('=')
                self.account_password = parts[1].strip()

            elif "account_name" in line:
                parts = line.split('=')
                self.account_name = parts[1].strip()

# create an instance of the class
tokens = RedditTokens('redditTokens.txt')

# access the tokens
client_id = tokens.client_id
client_secret = tokens.client_secret
account_password = tokens.account_password
account_name = tokens.account_name

# print the tokens
