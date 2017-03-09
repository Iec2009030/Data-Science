#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:56:04 2017

@author: Nitin Bansal
"""
import sys
import math
import operator
import random
import numpy as np
from operator import add
#from collections import defaultdict

""" Reading File Function """

def readFile(fileName):
    contents = []
    f = open(fileName)
    for line in f:
      contents.append(line)
    f.close()
    list_sentence= []
    for i in contents:
        list_sentence.append(i.split())
    list_sentence = [[x.lower() for x in y] for y in list_sentence]
    #print (list_sentence)
    return list_sentence
    
""" Function for Calculating Forward Probablities """
def forward(a,b,c):
    """Initializing With Correct Variables where n stands for number of words
    in the selected sentence. m stands for total number distinct Tags available
    and an array named dp to contain the probablity of the values stored."""
    
    n = len(b)
    m = 5 #Noun, Verb, Inf, Prep, Phi
    dp = [[0 for x in range(m)] for y in range(n+1)]
    #Assigning the Base Condition dp[0]['phi'] = 1
    dp[0][4] = 1
    dp = [[float(y) for y in x] for x in dp]
    print ("Calculating the Forward Probablity")
    for i in range(1,n+1):
        for j in range(0, m-1):
            temp = 0.0
            word = b[i-1]
            tag = c[j]
            tup_word = (word,tag)
            for k in range(0,m-1):
                if (i != 1):
                    tup_tag = (c[j],c[k])
                    if (tup_word in a):
                        emission_prob = a[tup_word]
                    else:
                        emission_prob = 0.0001
                    
                    if(tup_tag in a):
                        transmission_prob = a[tup_tag]
                    else:
                        transmission_prob = 0.0001
                  
                    temp =  temp + dp[i-1][k]*transmission_prob*emission_prob
                else:
                    tup_tag = (tag,'phi')
                    if (tup_word in a):
                        emission_prob = a[tup_word]
                    else:
                        emission_prob = 0.0001
                    
                    if(tup_tag in a):
                        transmission_prob = a[tup_tag]
                    else:
                        transmission_prob = 0.0001
                        
                    temp = transmission_prob*emission_prob
                    break
            dp[i][j] = temp
            print (temp)
                
    

""" Function for Collecting Data from respective Text File """   
def viterbi_forward(a,b):
    list_sent = []
    list_prob = []
    dict_prob = {}
    temp = ()
    list_sent = readFile(b)
    list_prob = readFile(a)
    """ Preparing a Dictionary for Probablity """
    for i in range(0, len(list_prob)):
        temp = tuple(list_prob[i][:2])
        dict_prob[temp] = float(list_prob[i][2])
    tag_list = ['noun','verb','inf','prep']
    #list_sent[0] = ['bears', 'fish']
    for i in range(len(list_sent)):
        viterbi_util(dict_prob, list_sent[i],tag_list)
        forward(dict_prob,list_sent[i],tag_list)

""" Main Viterbi Function """
def viterbi_util(a,b,c):
    """Initializing With Correct Variables where n stands for number of words
        in the selected sentence. m stands for total number distinct Tags available
        and an array named dp to contain the probablity of the values stored."""
    
    #n = len(b[0])
    n = len(b)
    m = 5 #Noun, Verb, Inf, Prep, Phi
    dp = [[0 for x in range(m)] for y in range(n+1)]
    bp = [[-1 for x in range(m)] for y in range(n+1)]
    #print (bp)
    #Assigning the Base Condition dp[0]['phi'] = 1
    dp[0][4] = 1
    dp = [[float(y) for y in x] for x in dp]
    #print (dp)
    """ Starting with Dynammic Programming """
    print ("Sentence in Consideration")
    print (b)
    for i in range(1,n+1):
        for j in range(0, m-1):
            max_prob = 0.0
            pos = 0
            word = b[i-1]
            tag = c[j]
            tup_word = (word,tag)
            for k in range(0,m-1):
                if (i != 1):
                    tup_tag = (c[j],c[k])
                    if (tup_word in a):
                        emission_prob = a[tup_word]
                    else:
                        emission_prob = 0.0001
                            
                    if(tup_tag in a):
                        transmission_prob = a[tup_tag]
                    else:
                        transmission_prob = 0.0001
                  
                    temp = dp[i-1][k]*transmission_prob*emission_prob
                    if (temp > max_prob):
                        max_prob = temp
                        pos = k
                else:
                    tup_tag = (tag,'phi')
                    if (tup_word in a):
                        emission_prob = a[tup_word]
                    else:
                        emission_prob = 0.0001
                    
                    if(tup_tag in a):
                        transmission_prob = a[tup_tag]
                    else:
                        transmission_prob = 0.0001
                        
                    max_prob = transmission_prob*emission_prob
                    pos = k
                    break
                
            dp[i][j] = max_prob
            bp[i][j] = pos
            print (dp[i][j])
    """ Back-Pointer Implementation to find the tag Sequence """
    final_pos = 0
    final_tag = 0
    fin_sequence = []
    for i in range(n,0,-1):
        final_prob = 0.0
        if (i == n):
            for j in range(0,m-1):
                if (dp[i][j] > final_prob):
                    final_prob = dp[i][j]
                    final_tag = j
                    final_pos = bp[i][j]
            print ("Probablity for best sequence is")
            print (final_prob)
            print("Tags are Respectively: ")
            #print (c[final_tag])
            fin_sequence.append(c[final_tag])
        else:
            #print (c[final_pos])
            fin_sequence.append(c[final_pos])
            final_pos = bp[i][final_pos]
    
                   
    fin_sequence.reverse()
    print ("Most Probable Tag Sequence According to Viterbi Algorithm for Sentence")
    print (b)
    print (fin_sequence)      
    print ("Backpointer Information")
    for j in range(0,m-1):
        print (c[bp[n][j]])
                


""" Main Fucntion Part """
def main():
    args = sys.argv
    #print (args[1])
    #print (args[2])
    viterbi_forward(args[1], args[2])
    

if __name__ == "__main__":
    main()
