# qotd-bot
A twitter bot to misattribute quotes

This is a twitter bot that is currently tweeting [@qotd_bot](https://twitter.com/qotd_bot).
It misattributes a historical quote every four hours.
It is written in python using the [Tweepy library](http://www.tweepy.org/).
The quotes are largely from [*The Yale Book of Quotations* by Fred R. Shapiro](https://en.wikipedia.org/wiki/The_Yale_Book_of_Quotations).

`bot.py` is the main file, and it requires a file named `secret.py` in the same directory formatted as follows:
~~~~
C_KEY = ''
C_SECRET = ''
A_TOKEN = ''
A_TOKEN_SECRET = ''
~~~~
where `C_KEY` is your consumer key, `C_SECRET` is your consumer secret key, `A_TOKEN` is your OAuth access token, and `A_TOKEN_SECRET` is your OAuth secret token.
It logs each of its tweets to `pasttweets.txt` to ensure it does not tweet duplicates.
