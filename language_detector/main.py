# -*- coding: utf-8 -*-
import string
"""
This collection of functions takes a receives a string of text and a list
and determines the most frequently used language in said text.
"""

def detect_language(text, languages):
    words = _create_word_list_from(text)
    matches = _tally_word_matches_between(words, languages)
    answer_index = _find_top_match_index(matches)

    return languages[answer_index]['name']

def _create_word_list_from(text):
    only_words = ''.join([c for c in text if c not in string.punctuation])
    word_list = only_words.lower().split()

    return word_list

def _tally_word_matches_between(text_words, languages):
    matches = [0]*len(languages)

    for idx, selected_language in enumerate(languages):
        for test_word in selected_language['common_words']:
            matches[idx] += text_words.count(test_word)

    return matches

def _find_top_match_index(match_list):
    highest_match_total = 0
    answer_index = 0

    for i, word_match_total in enumerate(match_list):
        if word_match_total > highest_match_total:
            highest_match_total = word_match_total
            answer_index = i

    return int(answer_index)
