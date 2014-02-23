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

import os
import hashlib

class string_colorizer(object):
    @property
    def colors(self):
        """array with the escape codes being used"""
        return self._colors
    @property
    def reset(self):
        """escape code used to reset the formatting"""
        return self._reset

    def __init__(self,
                 colors      = None,
                 reset       = "\033[0m",
                 hashfunc    = hashlib.md5,
                 use_hashlib = True):
        """
        Arguments:
        - `colors`: array of the used colors' numbers for the escape codes; default: range from 31 to 37 + bolds
        - `reset`: escape code used to reset the formatting; default: "\\033[0m"
        - `hashfunc`: function used to map the string to the integer used to determine the color
        - `use_hashlib`: set to False if the hashfunc returns integer and does not need to be converted like the hashlib functions
        """
        self._reset = reset
        if use_hashlib:
            self.hashfunc = lambda x: int(hashfunc(x.encode()).hexdigest(),
                                          base=16)
        else:
            self.hashfunc = hashfunc

        if colors == None:
            colors = [ "{1};{0}".format(color, bold)
                       for bold in [0,1]
                       for color in range(31,38) ]
        self._colors = [ "\033[{0}m".format(color)
                         for color in colors ]

    def choose_color(self, string):
        """Chooses a color for the given string"""
        return self.colors[self.hashfunc(string) % len(self.colors)]

    def colorize(self, string):
        """Colors the given string according to its hash"""
        return self.choose_color(string) + string + self.reset

__all__ = ['string_colorizer']
