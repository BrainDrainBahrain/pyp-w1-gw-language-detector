# -*- coding: utf-8 -*-
import string 
"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    
    # implement your solution here
    '''
    LANGUAGES[0...n]['common_words'][0...n]
    '''
    #strips puncuation from text
    #txt = text.translate(None, string.punctuation)
    txt = ''.join([c for c in text if c not in string.punctuation])
    
    #generate table of words from 'text'
    text_table = txt.lower().split()
    
    res = []
    
    #iterate through languages
    for i, lang in enumerate(languages):
        #add space for counting matches to res
        res.append(0)
        
        #iterate through words in active 100 word dictionary
        for dictword in lang['common_words']:
            res[i] += text_table.count(dictword)
            
    ans = 0
    ansidx = 0
    for i, cnt in enumerate(res):
        if cnt > ans:
            ans = cnt
            ansidx = i
            
        
    return languages[ansidx]['name']
            
  
    
        
    

