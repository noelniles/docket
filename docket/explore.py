import os, sys
from collections import Counter
from xml.etree.cElementTree import iterparse


class Explorer:
    def __init__(self, path):
        self.path = path
        self.context = iterparse(self.path)

    def tag_set(self):
        """Return a set of all the tags."""
        tags = set()

        # Ugly, but neccessary hack
        try:
            next(self.context)
        except StopIteration:
            self.__init__(self.path)

        for event, elem in self.context:
            tags.add(elem.tag)
            elem.clear() # free memory
        return tags

    def filter(self, tag):
        """Search for tag and return a list of the text contained in
        each occurence of that tag.

        Keyword arguments:
        tag -- the tag to search for
        """
        try:
            next(self.context)
        except StopIteration:
            self.__init__(self.path)

        text = []
        for event, elem in self.context:
            if elem.tag == tag:
                text.append(elem.text)
                elem.clear() # free memory
        return text

    def count_tag(self, tag):
       """Count how often a tag appears.
       
       Returns a list of tuples (text, count) sorted by count. Each tuple
       contains the unique text from within the tag followed by a count of how
       many times the text appeared. Useful for histograms.
       
       Keyword arguments:
       tag -- the tag to search for
       """
       count = Counter(self.filter(tag))
       return count.most_common() 

