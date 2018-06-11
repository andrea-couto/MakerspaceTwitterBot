from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()
my_bot.sync_follows()
my_bot.auto_follow("makerspace")
my_bot.auto_follow("#BSU")
my_bot.auto_follow_followers()
# my_bot.send_tweet("Hello Makers!")