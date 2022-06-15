import json_lines as jl
import os
import csv
import re

with open('tweets.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)

    files = os.listdir('data')

    for file in files:
        party = input("Party of " + file + " (S / C / G / F / A / L): ")
        
        text = []

        with jl.open('data\\' + file) as data:
            for item in data:
                if 'data' in item['response']:
                    for tweet in item['response']['data']:
                        text.append(tweet['text'])
                    break

        for item in text:
            item = re.sub(r'http\S+', '', item)
            item = re.sub(r'\W', ' ', item)
            item = re.sub(r'\s+[a-zA-Z]\s+', ' ', item)
            item = re.sub(r'\^[a-zA-Z]\s+', ' ', item)
            item = re.sub(r'\s+', ' ', item, flags=re.I)
            item = re.sub(' RT|RT | TK|TK | amp','',item)
            item = re.sub(r'^[^[a-zA-Z]]*', '', item)
            item = item.lower()

            if item != "" and item != " ":
                print(item + "\n")
                writer.writerow([party, item])
