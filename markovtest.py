# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:38:55 2020

@author: Bri
"""

# LET'S PLAY MARKOV

import time
import sys
from matplotlib import pyplot as plt
import matplotlib
import numpy as np 
import datetime
from string import punctuation as pun
import random
#random.seed(1)

filename = 'spell.xml'
markov = {}

def main():
    markov=createMarkovChain()
    #print(markov)
    spell=""
    try:
        word=input("give me a word, I'll give you a spell\n")
        markov[word]
    except:
        print('NOT FOUND')
        return
    spell=word+' '
    while(len(markov[word])>0):
        dice = random.random()
        for w in markov[word]:
            if dice > markov[word][w]:
                dice-= markov[word][w]
            else:
                spell=spell+w+ ' '
#                print(spell)
#                time.sleep(0.5)
                word = w
                break
    print(spell)
        
    
    
def createMarkovChain():
    try:
        file = open(filename,'r+',encoding='UTF-8')
        rdata = file.readlines()
    except:
        print('File not found')
        return {}
        
    words = {}
    for line in rdata:
        line = line.lower()
        line = noPun(line)
        bits = line.split()
        
        for i in range(len(bits)):
            if bits[i] not in words:
                words[bits[i]] = {}
            if i != len(bits)-1:
                if bits[i+1] in words[bits[i]]:
                    words[bits[i]][bits[i+1]]+=1
                else:
                    words[bits[i]][bits[i+1]]=1
    
    for w in words:
        if len(words[w]) > 0:
            total = 0
            for c in words[w]:
                total += words[w][c]
            for c in words[w]:
                words[w][c] = words[w][c]/total
    return words
            



def noPun(s):
    s = list(filter(lambda x: x not in pun,s))
    s=''.join(map(str,s))
    return s


if __name__ == '__main__':
    main()