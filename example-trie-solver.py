#!/bin/python

from scrabble import Scrabble
import sys
from trie_lexicon import TrieLexicon
import time

language = 'en'
character_distribution = 'scrabble_letter_distribution-{}.txt'.format(language)
vocabulary = 'vocab_{}-cleaned.txt'.format(language)

print('Setting up lexicon ...')
start_time = time.time()
lexicon = TrieLexicon(vocabulary)
duration = time.time() - start_time
print("{:,} words loaded in {:.5f} seconds and {:,} bytes".format(lexicon.nwords, duration, sys.getsizeof(lexicon)))

scrabble = Scrabble(character_distribution)
tiles = scrabble.draw_tiles(7)
print('\nYou have drawn the following letters:')
print(', '.join(tiles))

start_time = time.time()
words = lexicon.find_words(tiles)
duration = time.time() - start_time
print('\nFrom these letters I found {:,} words in {:.5f} seconds'.format(len(words), duration))
      
scored_words = scrabble.score_words(words)
print('\nThe top 10 scoring words are:')
for score, word in scored_words[:10]:
    print(score, word)
       
