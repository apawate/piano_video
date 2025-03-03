#
#  Piano Video
#  A free piano visualizer.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""
pvkernel, the kernel for Piano Video.

This library is a Python module, and handles rendering, effects, MIDI parsing, etc.
"""

__version__ = "0.3.2"

import os
from .startup import PARENT, build, register_addons

LAST_COMP = os.path.join(PARENT, "last_compiled.txt")


def get_last_comp():
    if not os.path.isfile(LAST_COMP):
        return None
    with open(LAST_COMP, "r") as fp:
        return fp.read()

def set_last_comp():
    with open(LAST_COMP, "w") as fp:
        fp.write(__version__)


if get_last_comp() != __version__:
    build()
set_last_comp()
del build
del get_last_comp
del set_last_comp

from . import draw
from .video import Video

register_addons()
del register_addons
