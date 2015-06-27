import os, sys
from collections import Counter
from xml.etree.cElementTree import iterparse
from lib.coroutine import *

class Explorer:
    def __init__(self, path):
        self.path = path
        self.context = iterparse(self.path)
        self.context = iter(self.context)

    def tag_set(self):
        """Return a set of all the tags"""
        tags = set()
        for event, elem in self.context:
            tags.add(elem.tag)
        return tags

    def filter(self, tag):
        """Search for tag and return the text.

        Keyword arguments:
        target -- another coroutine
        """
        event, root = next(self.context)
        for event, elem in self.context:
            if elem.tag == tag:
                print(elem.text)
                root.clear()

