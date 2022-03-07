#!/usr/bin/env python3

# --------------------------------
# Programming/Wordle/run_wordle.py
# Copyright (C)
# Haohang (Adrian) Guo
# --------------------------------

# -------
# imports
# -------

import string

# ------------
# wordle_guess
# ------------

def wordle_guess(t):
    max_idx = t["Sum"].idxmax()
    return t.loc[max_idx, "Words"]

# -----------
# wordle_read
# -----------


def wordle_read(a):
    print("\nThe current guess is: " + a)
    print("Please enter the correctness below")
    print("g: green, y: yellow, n: incorrect (lowercase ONLY)")
    print("For example, a valid input would be: ngnny")
    print("If prompted not a valid word, enter: \'again\'")
    while True:
        response = input("Please enter the response here: ")
        if response == 'again':
            return response

        if len(response) != len(a):
            print("\nINCORRECT INPUT LENGTH")
        elif not set(response).issubset({'g', 'y', 'n'}):
            print("\nENTER ONLY \'g', \'y\', and \'n\'")
        else:
            return response

# -----------
# wordle_eval
# -----------


def wordle_eval(a, r, t, i, n):
    if r == 'again':
        n += 1
        t = t[t['Words']!=a]
        return False, t, n

    if set(r) == {'g'}:
        return True, t, n
    
    indices = list(range(len(r)))
    reduce_letters = []

    for c, k in enumerate(r):
        if k == 'g':
            t = t[t[i[c]] == a[c]]
            indices.remove(c)
        elif k == 'y':
            t = t[t[i[c]] != a[c]]
            t = t[(t == a[c]).any(axis=1)]
        else:
            reduce_letters.append(a[c])
    
    i_copy = [i[ind] for ind in indices]
    for l in reduce_letters:
        t = t[(t[i_copy] != l).all(axis=1)]
    
    return False, t, n

# ------------
# wordle_print
# ------------


def wordle_print(n, t, s):
    if s:
        print("Thank you for using me!\n")
        return
    if t.empty:
        print("I'm sorry, but this word is not in my vocabulary.")
        return
    n -= 1
    if n == 0:
        print("I'm sorry that I failed, and it's not possible.")
    return n
    

# ------------
# wordle_solve
# ------------


def wordle_solve(t, n, i):
    state = False
    while not state and n:
        attempt = wordle_guess(t)
        response = wordle_read(attempt)
        state, t, n = wordle_eval(attempt, response, t, i, n)
        n = wordle_print(n, t, state)