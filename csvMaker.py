import json_lines as jl
import re
import csv
import glob

filterList = []
filterStr = ''

while True:
    filterStr = input("Enter parties to be filtered (comma-separated) and press Enter\n")
    partyCounter = input("Please type in the max amount of tweets per party, a semicolon and Enter\n")
    if ';' in partyCounter:
        break

partyCounter = int(partyCounter.replace(";", ""))
partyCounterArr = [0,0,0,0,0,0,0,0]
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
                            if party == "Bündnis 90/Die Grünen":
                                if partyCounterArr[0] >= partyCounter:
                                    break
                                partyCounterArr[0] = partyCounterArr[0] + 1 
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "SPD":
                                if partyCounterArr[1] >= partyCounter:
                                    break
                                partyCounterArr[1] = partyCounterArr[1] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "CDU":
                                if partyCounterArr[2] >= partyCounter:
                                    break
                                partyCounterArr[2] = partyCounterArr[2] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "CSU":
                                if partyCounterArr[3] >= partyCounter:
                                    break
                                partyCounterArr[3] = partyCounterArr[3] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "FDP":
                                if partyCounterArr[4] >= partyCounter:
                                    break
                                partyCounterArr[4] = partyCounterArr[4] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "AfD":
                                if partyCounterArr[5] >= partyCounter:
                                    break
                                partyCounterArr[5] = partyCounterArr[5] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "Die Linke":
                                if partyCounterArr[6] >= partyCounter:
                                    break
                                partyCounterArr[6] = partyCounterArr[6] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')
                            elif party == "Fraktionslos":
                                if partyCounterArr[7] >= partyCounter:
                                    break
                                partyCounterArr[7] = partyCounterArr[7] + 1
                                text.insert(i, party + ',')
                                text.insert(i, text[i] + tweet + '\n')
                                csv.write(text[i])
                                validParty = True
                                validTweet = False
                                i = i + 1
                                print('Progress: ' + str((fileNum / len(files)) * 100) + '%')

        fileNum = fileNum + 1

    csv.close()
