#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017, 2018 Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

from setzer.document.source_buffer.source_buffer import SourceBuffer
import setzer.document.source_buffer.parser.parser_bibtex as parser_bibtex


class SourceBufferBibTeX(SourceBuffer):

    def __init__(self):
        SourceBuffer.__init__(self)

        self.symbols = dict()
        self.symbols['bibitems'] = set()

        self.parser = parser_bibtex.ParserBibTeX(self)

    def get_bibitems(self):
        return self.symbols['bibitems']

    def get_gsv_language_name(self):
        return 'bibtex'


