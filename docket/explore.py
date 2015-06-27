import os, sys
from collections import Counter
from xml.etree.cElementTree import iterparse

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
        """Search for tag and return a list of the text.

        Keyword arguments:
        tag -- the tag to search for
        """
        text = []
        event, root = next(self.context)
        for event, elem in self.context:
            if elem.tag == tag:
                text.append(elem.text)
                root.clear()
        return text

    def freq(self, tag, text):
       """Counts how many times text appears in all of the tags"""
       pass

