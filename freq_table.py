#!/usr/bin/env python3

# --------------------------------
# Programming/Wordle/freq_table.py
# Copyright (C)
# Haohang (Adrian) Guo
# --------------------------------

'''
The word_frequency library can be used to optimize the algorithm.
However, it is not necessary.
'''

# -------
# imports
# -------

#from english_words import english_words_lower_set
#from wordfreq import word_frequency
import pandas as pd
import string

# -------------------
# generate_word_table
# -------------------

def generate_word_table(l, n, i):
    '''
    # The default english word library can also be used to solve wordle
    five_char_words = [word for word in english_words_lower_set if len(word) == n
                       and set(word) < l]
    split_chars = [list(word) for word in five_char_words]
    '''

    word_list = open("word_list.txt", "r")
    five_char_words = word_list.read().split('\n')
    
    # make a pandas DataFrame for data manipulation
    tb = pd.DataFrame(split_chars, columns=i)
    tb.insert(loc=0, column="Words", value=five_char_words)
    
    return tb

# ---------------------
# generate_letter_table
# ---------------------

def generate_letter_table(w, i):
    # count the frequency of letters at each position of all 5-letter words
    letter_count = w[i].apply(pd.value_counts).fillna(0)
    letter_table = letter_count/letter_count.sum()
    
    return letter_table

# -------------------
# generate_freq_table
# -------------------

def generate_freq_table(w, l, n, i):
    # cross-reference every letter with the frequency at its location
    for ind in i:
        w[i.index(ind)] = w[ind].apply(lambda x: l.loc[x, ind])
    
    # find the overall frenquency with respect to its letters
    w["Sum"] = w[list(range(n))].sum(axis=1)
    
    return w

# ----------------
# build_freq_table
# ----------------

def build_freq_table(I):
    # predefined variables
    word_length = len(I) # five character words
    valid_letters = set(string.ascii_lowercase) # only a-z allowed
    
    # we store the frequencies in a pandas dataframe for speed and efficiency
    word_table = generate_word_table(valid_letters, word_length, I)
    
    # calculate frequency of letters and weigh each word accordingly
    letter_table = generate_letter_table(word_table, I)
    
    # calculate the weighted frequency of words
    freq_table = generate_freq_table(word_table, letter_table, word_length, I)

    return freq_table