import json_lines as jl
import os
import csv

with open('tweets.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Party", "Tweet"])

    files = os.listdir('data')

    for file in files:
        party = input("Party of " + file + " (S / C / G / F / A / L): ")
        
        text = []

        with jl.open('data\\' + file) as data:
            for item in data:
                for tweet in item['response']['data']:
                    text.append(tweet['text'])
                break

        for item in text:
            print(item + "\n")
            writer.writerow([party, item])
