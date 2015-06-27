import os, sys
from collections import Counter
import xml.etree.ElementTree as ET
from lib.coroutine import *

class Explorer:
    def __init__(self, path):
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

    def child_by_index(self, index):
        print("Tag: ", self.root[index].tag)
        print("Text: ", self.root[index].text)

    def dump(self):
        for child in self.root:
            print("Tag: ", child.tag)
            print("Attrib: ", child.attrib)

    def interesting_dump(self, tag=None):
        for child in self.root.iter(tag):
            print("Tag: ", child.tag)
            print("Attrib: ", child.attrib)
            print("Text: ", child.text)

    def naive_count_judges(self):
        # Returns a Counter object with all the judges
        judges = []
        for child in self.root.iter('md.judge'):
            judges.append(child.text) 
        count = Counter(judges)
        return count 

    def tag_set(self):
        # Returns a set of all tags of the tree
        tags = []
        for x in self.tree.iter():
            tags.append(x.tag)
        return set(tags)

    @coroutine
    def printer():
        while True:
            event = (yield)
            print(event)

