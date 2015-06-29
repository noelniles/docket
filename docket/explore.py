"""
Copyright 2015 Noel Niles
explore.py is part of Docket.

    Docket is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Docket is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Docket.  If not, see <http://www.gnu.org/licenses/>.
"""
import os, sys
from collections import Counter
from xml.etree.cElementTree import iterparse


class Explorer:
    """Explores XML files.

    Initial Paramaters:
    path -- a path to an XML file

    Class Attributes:
    self.path -- the path to the XML file
    self.context -- an iterator with (event, elem) pairs
    
    Methods:
    tag_set -- returns a set of all the tags
    grab -- grabs the text from one tag
    grab_many -- grabs the text from a list of tags
    count_tag -- returns a list of tuples with the tag text and how
                 often a tag appears
    """
    def __init__(self, path):
        self.path = path
        self.context = iterparse(self.path)

    def tag_set(self):
        """Return a set of all the tags.
        
        Useful for finding out which tags have usefule information in an
        xml file.
        """
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

    def grab(self, tag):
        """Search for tag and return a list of the text.
        
        Returns a list of of all of the strings from each occurrence of
        tag in the xml documents. *Note* this will ignore items that
        don't have a text attribute.

        Keyword arguments:
        tag -- string, the tag to search for
        """
        try:
            next(self.context)
        except StopIteration:
            self.__init__(self.path)

        text = []
        for event, elem in self.context:
            if elem.tag == tag:
                # Don't add empty text
                if elem.text is not None:
                    text.append(elem.text)
                elem.clear() # free memory
        return text

    def grab_many(self, tags=[]):
        """Search for tag and return a dictionary of text.

        Returns a dictionary indexed by tags. Each key points to a list
        of the text from every occurrence of the tag in the xml file.

        Keyword argument:
        tags -- list of strings which are tags in the xml file.
            *Valid tags can be found using the tag_set function.*
        """
        result = {}
        text = []
        for event, elem in self.context:
            for tag in tags:
                if elem.tag == tag and elem.text is not None:
                    text.append(elem.text)

                result[tag] = text
        return result

    def count_tag(self, tag):
       """Count how often a tag appears.
       
       Returns a list of tuples (text, count) sorted by count. Each tuple
       contains the unique text from within the tag followed by a count of how
       many times the text appeared. Useful for histograms.
       
       Keyword arguments:
       tag -- string, the tag to search for
       """
       count = Counter(self.filter(tag))
       return count.most_common() 

