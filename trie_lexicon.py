#!/bin/python
from trie_node import TrieNode

from functools import reduce
class TrieLexicon(object):
    def __init__(self, vocabulary):
        self.root = TrieNode()
        self.nwords = 0
        self.setup(vocabulary)

    def setup(self, vocabulary):
        with open(vocabulary, 'r', encoding='utf-8') as f:
            for word in f.readlines():
                self.addWord(word.strip())
                self.nwords += 1

    def addWord(self, word):
        p = self.root
        for letter in word:
            p = p.addChild(letter)
        p.isTerminalNode = True
        
    def isWord(self, word):
        p = self.root
        for letter in word:
            p = p.findChild(letter)
            if p == None:
                return False
        return p.isTerminalNode

    def find_words(self, chars):
        words = list()
        self.find_words_recur(self.root, '', chars, words)
        return words

    def find_words_recur(self, node, string, remaining_chars, words):
        if node.isTerminalNode:
            words.append(string)
        if len(node.children.keys()) == 0 or len(remaining_chars) == 0:
              return
        for char in node.children:
            if char in remaining_chars or '_' in remaining_chars:
                index = remaining_chars.index(char) if char in remaining_chars else remaining_chars.index('_')
                self.find_words_recur(node.children[char],
                                      string + char,
                                      remaining_chars[:index] + remaining_chars[index + 1:],
                                      words)
