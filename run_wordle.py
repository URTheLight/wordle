#!/usr/bin/env python3

# --------------------------------
# Programming/Wordle/run_wordle.py
# Copyright (C)
# Haohang (Adrian) Guo
# --------------------------------

'''
Note:
this solution does not consider Bayes factors, so it can be improved
'''

# -------
# imports
# -------

from freq_table import build_freq_table
from wordle import wordle_solve

# -------
# set-up
# -------

NUM_ATTEMPTS = 6
INDEX = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

# ----
# main
# ----

if __name__ == "__main__":
    word_table = build_freq_table(INDEX)
    wordle_solve(word_table, NUM_ATTEMPTS, INDEX)