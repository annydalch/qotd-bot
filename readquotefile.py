import os
import random

QUOTES_FILENAME = "quotes.txt"
AUTHORS_FILENAME = "authors.txt"
PAST_TWEETS_FILENAME = "pasttweets.txt"

file = open(QUOTES_FILENAME, 'r')
try:
    quotes = file.read().splitlines()
finally:
    file.close()
    
file = open(AUTHORS_FILENAME, 'r')
try:
    authors = file.read().splitlines()
finally:
    file.close()

def make_quote():
    ourquote = quotes[random.randrange(0, len(quotes))]
    ourauthor = authors[random.randrange(0, len(authors))]
    fulltext = '"' + ourquote + '" --' + ourauthor
    return fulltext


def check_against_past_quotes(quote):
    duplicate = False
    pastQuotesFile = open(PAST_TWEETS_FILENAME, 'r')
    try:
        for line in pastQuotesFile:
            temp = line.strip('\n')
            if temp == quote:
                duplicate = True
                break
    finally:
        pastQuotesFile.close()
    return duplicate

def gen_unique_quote():
    needanother = True
    quote = ''
    count = 0
    while needanother and count < 30:
        quote = make_quote()
        needanother = check_against_past_quotes(quote) and (len(quote) < 161)
        count += 1
    if count == 30:
        return False
    return quote

def quote_generator():
    quote = gen_unique_quote()
    pastQuotesFile = open(PAST_TWEETS_FILENAME, 'a')
    try:
        pastQuotesFile.write(quote + '\n')
    finally:
        pastQuotesFile.close()
    return quote

