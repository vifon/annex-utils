#!/usr/bin/env python3
# -*- python -*-
#########################################################################
# Copyright (C) 2013-2014  Wojciech Siewierski                          #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################
"""path colorizer

Colors the path segments in each path given on stdin or in the file specified in the argument.
"""

from __future__ import print_function

import fileinput
import os
from sys import argv

from string_colorizer import string_colorizer

class path_colorizer(string_colorizer):
    def colorize_path(self, path):
        """Colors each path component to the appropriate color"""
        return os.sep.join([ self.colorize(component)
                             for component in path.split(os.sep) ])

def main():
    colorizer = path_colorizer()
    for line in fileinput.input():
        path = line.rstrip(os.linesep)
        print(colorizer.colorize_path(path))

if __name__ == "__main__":
    main()
