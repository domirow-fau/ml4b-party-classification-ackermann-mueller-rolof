import json_lines as jl
import re
import csv
import glob

filterList = []
filterStr = ''

while True:
    filterStr = input("Enter parties to be filtered (comma-separated), type in a semicolon and press Enter\n")
    if ';' in filterStr:
        break

filterStr = filterStr.replace(";", "")
filterStr = filterStr.lower()
filterList = filterStr.split(',')

with open('tweets.csv', 'a', newline='', encoding="utf-8") as csv:
    files = glob.glob('*.jl')
    fileNum = 0

    for file in files:

        text = []

        with jl.open('./' + file) as f:
            i = 0
            validParty = True
            validTweet = False
            for item in f:
                party = item['account_data']['Partei']
                if party.lower() in filterList:
                    validParty = False
                    break
                if 'data' in item['response']:
                    for tweet in item['response']['data']:
                        tweet = tweet['text']
                        tweet = re.sub(r'http\S+', '', tweet)
                        tweet = re.sub(r'\W', ' ', tweet)
                        tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', tweet)
                        tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', tweet)
                        tweet = re.sub(r'\s+', ' ', tweet, flags=re.I)
                        tweet = re.sub(' RT|RT | TK|TK | amp','',tweet)
                        tweet = re.sub(r'^[^[a-zA-Z]]*', '', tweet)
                        tweet = tweet.lower()
                        tweet = tweet.strip()
                        if (tweet != '' and tweet != ' '):
                            validTweet = True
                        if validParty and validTweet:
                            text.insert(i, party + '|')
                            text.insert(i, text[i] + tweet + '\n')
                            csv.write(text[i])
                validParty = True
                validTweet = False
                i = i + 1

        fileNum = fileNum + 1
        print('Progress: ' + str((fileNum / len(files)) * 100) + '%')

    csv.close()
