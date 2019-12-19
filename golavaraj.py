# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:46:50 2019

@author: tolao
"""

import csv
import statistics
with open('T1.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    first1=[]
    for line in csv_reader:
        #print(line['HomeTeam'],line['AwayTeam'],line['FTHG'],line['FTAG'])
        total_goals=[line['HomeTeam'],line['AwayTeam'],line['FTHG'],line['FTAG'],line]
        total_goals[4]=int(total_goals[2])+int(total_goals[3])
        first1.append(total_goals)
    golavaraj=[]
    takim=input('Takimi gir AQ: ')
    i=0
    while i < len(first1):
        if first1[i][0]==takim:
            golavaraj.append(first1[i][4])
        i+=1
    i=0
    while i < len(first1):
        if first1[i][1]==takim:
            golavaraj.append(first1[i][4])
        i+=1
print(statistics.mean(golavaraj))
#print(golavaraj)