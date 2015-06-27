import os
from docket.explore import Explorer
from docket.cosax import EventHandler
import xml.sax


if __name__ == '__main__':
    # Build the path to the xml file
    data_path = 'law_data/InnocentiveYear2005DCTExtract'
    xml_file = 'DCTInnoExtY20050420DCTInnoExtY20050420_N_DFEDDISTCV12_2015042064336.nxo.xml'
    path = os.path.join(os.getcwd(), data_path, xml_file)

    x = Explorer(path)
    #x.naive_count_judges()

    # Example of using Event Handlers
    #xml.sax.parse(path, EventHandler(printer()))

    # Returns all of the tags
    print(x.tag_set())
