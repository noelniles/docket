"""
Copyright 2015 Noel Niles
This file is part of Docket.

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
import os
from docket.explore import Explorer


if __name__ == '__main__':
    # Build the path to the xml file
    data_path = 'law_data/InnocentiveYear2005DCTExtract'
    xml_file = 'DCTInnoExtY20050420DCTInnoExtY20050420_N_DFEDDISTCV12_2015042064336.nxo.xml'
    path = os.path.join(os.getcwd(), data_path, xml_file)

    x = Explorer(path)

    #print("All Possible Tags:")
    #for tag in x.tag_set():
    #    print(tag)
   
    #print(x.filter('cause'))
    #print("Causes from Most to Least Common:")
    #for cause in x.count_tag('cause'):
    #    print(cause)
    res = x.fields_from_tag(['court.block', 'md.title'])

    for title in res['md.title']:
        print("Title: ", title)
    for cb in res['court.block']:
        print("Court: ", cb)
