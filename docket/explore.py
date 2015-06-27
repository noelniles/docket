import os, sys
import xml.etree.ElementTree as ET

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

    def count_judges():
        pass

