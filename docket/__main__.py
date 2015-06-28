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
import os, sys
from docket.explore import Explorer



if __name__ == '__main__':
    # Build the path to the xml file
    data_path = 'law_data/InnocentiveYear2005DCTExtract'
    xml_file = 'DCTInnoExtY20050420DCTInnoExtY20050420_N_DFEDDISTCV12_2015042064336.nxo.xml'
    path = os.path.join(os.getcwd(), data_path, xml_file)

    help_msg = ("""Usage: $ python -m docket tag-set: The set of all tags\n"""
        """       $ python -m docket grab <tag>: Grabs the text from tag\n""")

    x = Explorer(path)
    numargs = len(sys.argv)

    consumer = x.consume()
    consumer.send(None)
    producer = x.produce(consumer, x.tag_set())

    # Exit if no command line arguments
    if numargs > 1:
        op = sys.argv[1]
    else:
        print(help_msg)
        sys.exit(1)

    if op == 'tag-set':
        print("All Possible Tags:")
        for i in producer:
            print(i)
        sys.exit(0)
    elif op == 'grab':
        if numargs != 3:
            print(help_msg)
            sys.exit(1)
        else:
            tag = sys.argv[2]
            print(x.grab(tag))
    elif op == 'grab-many':
        if numargs <= 3:
            print(help_msg)
            sys.exit(1)
        else:
            tags = list(sys.argv[2:])
            print(x.grab_many(tags))
    elif op == 'count-tag':
        if numargs != 3:
            print(help_msg)
            sys.exit(1)
        else:
            print(x.count_tag(sys.argv[2]))
    elif args == '':
        print(help_msg)
        sys.exit(0)
   
