"""
Copyright 2015 Noel Niles
docket_tests.py is part of Docket.

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
import time
import unittest
from nose.tools import *

from docket.explore import Explorer


class TestExplorer(unittest.TestCase):

    @classmethod
    def setup_class(self):
        self.data_path = 'law_data/InnocentiveYear2005DCTExtract'
        self.xml_file = 'DCTInnoExtY20050420DCTInnoExtY20050420_N_DFEDDISTCV12_2015042064336.nxo.xml'
        self.path = os.path.join(os.getcwd(), self.data_path, self.xml_file)
        self.x = Explorer(self.path)
        print("SETUP!")
    
    @classmethod
    def teardown_class(self):
        del self.x
        print("TEAR DOWN!")

    def test_tag_set(self):
        print("Testing tag_set()")
        test_set = {'md.jurisdiction', 'n-metadata', 'knos.level1',
                'cause.block', 'number', 'judge', 'court.citelist',
                'md.jurisstate', 'case.type', 'md.title', 'col.key',
                'image.block', 'case.ref.to', 'md.jurisnum',
                'party.aka.block', 'md.subjects', 'state.source',
                'case.number.hidden', 'md.sourcepubid',
                'firm.fax.block', 'md.subject', 'court.pretty',
                'n-docbody', 'mlmd.judgment.record', 'md.doctype.name',
                'summary', 'party.type', 'court', 'n-metadoc',
                'party.block', 'docket.entry', 'n-document', 'state',
                'c', 'sct.jurisdiction.number', 'case.number.block',
                'party.terminated', 'jury.demand.block',
                'lead.docket.number', 'bop', 'knos.level2', 'bos',
                'case.status.flag', 'pc', 'docket.number',
                'n-extract-response', 'other.dockets.block',
                'md.contributors', 'n-field', 'gateway.image.link',
                'cta.jurisdiction.number', 'docket.block',
                'knos.level3.block', 'other.party', 'p', 'label',
                'md.uuid', 'nature.of.suit.code',
                'firm.address.combined', 'md.jurisabbrev',
                'court.block', 'firm.address.block', 'firm.phone.block',
                'md.pubid', 'eop', 'jurisdiction',
                'key.nature.of.suit.block', 'filing.date.block',
                'jury.demand', 'image.gateway.link', 'cite.query',
                'minor.link.metadata.block', 'party.name', 'city',
                'md.dates', 'md.createddatetime', 'firm.name.block',
                'docket.description', 'case.ref.to.block', 'link',
                'demand.amount', 'higher.court.information',
                'party.aka', 'number.block', 'jurisdiction.block',
                'panel.block', 'cause', 'knos.level2.block',
                'lead.docket.block', 'md.juriscourt', 'court.norm',
                'date', 'r', 'prism-clipdate', 'party.name.block',
                'title.block', 'knos.code', 'md.jurisdictions',
                'attorney.status', 'closed.date.block',
                'md.descriptions', 'docket.entries.block',
                'other.dockets', 'metadata.block', 'case.status.block',
                'scrape.date', 'md.filedate', 'md.docketnum',
                'convert.date', 'zip', 'firm.phone', 'md.publication',
                'party.attorney.block', 'attorney.terminated',
                'legacy.id', 'md.royalty', 'send.runner.link',
                'md.doctype.rank', 'private', 'case.number',
                'filing.date', 'closed.date', 'prism-stylesheet',
                'nature.of.suit.block', 'defendant.party',
                'attorney.name', 'data.source.type',
                'party.terminated.block', 'md.publications', 'firm.fax',
                'lead.docket.number.INF', 'md.doc.family.uuid',
                'md.westlawids', 'firm.name', 'platform', 'street',
                'md.judge', 'md.identifiers', 'md.publicationgroup',
                'knos.level1.block', 'md.infotype', 'md.royalty.code',
                'eos', 'nature.of.suit', 'demand.amount.block',
                'attorney.terminated.block', 'knos.level3',
                'md.royalty.number', 'cluster.name', 'md.jurislevel',
                'md.attorney', 'primary.title', 'plaintiff.party',
                'attorney.email'}
        
        assert_equals(self.x.tag_set(), test_set)
        
