ANNEX-UTILS
===========

Various Git Annex utilities

ANNEX-WHEREIS, ANNEX-LIST, ANNEX-LOG
------------------------------------

Drop-in colorizers for `git annex whereis`, `git annex list` and `git
annex log`.

ANNEX-BIND
----------

Relink the missing content from another locally available annex
repository. Use `git checkout -f' afterwards.

ANNEX-DIR
---------

Lists which directories have at least one file present and which are
completely empty.

**Example:** We have a repository with music with directory layout
based on artists and/or albums. We either have the whole album (or
artist) or we have none of its files. A traditional check would take
too long and be too verbose to be useful. This approach is much more
efficient in such cases..

AUTHOR
------

Wojciech Siewierski < wojciech dot siewierski at gmail dot com >

COPYRIGHT
---------

Copyright (C) 2013-2015  Wojciech Siewierski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
