#!/bin/python

from collections import namedtuple
import random

class Scrabble(object):
    def __init__(self, character_distribution):
        self.tiles = list()
        self.points = dict()
        self.setup(character_distribution)

    def setup(self, character_distribution):
        # store character points frequency in a text file
        with open(character_distribution, 'r') as f:
            for line in f.readlines():
                value, points, frequency = line.split()
                self.tiles += [value for i in range(int(frequency))]
                self.points[value] = int(points)   

    def draw_tiles(self, n):
        random.shuffle(self.tiles)
        return sorted([self.tiles.pop() for _ in range(n)])

    def score_word(self, word):
        return sum(self.points[c] for c in word)

    def score_words(self, words):
        scored_words = [(self.score_word(word), word) for word in words]
        scored_words.sort(key=lambda x: x[0], reverse=True)
        return scored_words
