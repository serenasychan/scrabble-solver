#!/bin/python
from collections import defaultdict
class TrieNode(object):
    def __init__(self, value = None):
        self.children = dict()
        self.value = value
        self.isTerminalNode = False
        
    def findChild(self, value):
        if value in self.children.keys():
            return self.children[value]
        else:
            return None
        
    def addChild(self, value):
        childNode = self.findChild(value)
        if childNode == None:
            childNode = TrieNode(value)
            self.children[value] = childNode
        return childNode
