import os, sys
import xml.etree.ElementTree as ET


class Explorer:

    def __init__(self):
        try:
            self.approot = os.path.abspath(__file__)
        except NameError:
            self.approot = os.path.dirname(sys.argv[0])
    
    def show_something(self):
        data_path = 'law_data/InnocentiveYear2005DCTExtract'
        xml_path = 'DCTInnoExtY20050420DCTInnoExtY20050420_N_DFEDDISTCV12_2015042064336.nxo.xml'
        xml_file = os.path.join(os.getcwd(), data_path, xml_path)
        tree = ET.parse(xml_file)
        root = tree.getroot()

        doc = root[1]

        for x in doc.iter('n-document'):
            print(x)
