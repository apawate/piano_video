#
#  Piano Video
#  Piano MIDI visualizer
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

import time
import pygame
import pv
from gui_utils import *
pygame.init()


class GuiDisplay:
    def __init__(self):
        self.prev_size = None
        self.next_draw_time = 0

    def redraw(self, surface, rect):
        self.draw(surface, rect)

    def draw(self, surface, rect):
        x, y, w, h = rect

        resized = False
        if (w, h) != self.prev_size:
            pv.disp.image = pygame.Surface((w, h))
            resized = True
        self.prev_size = (w, h)

        time_passed = False
        if time.time() >= self.next_draw_time:
            time_passed = True
            self.next_draw_time = time.time() + 1/pv.disp.fps

        if not (resized or time_passed):
            return

        pv.disp.draw()
        surface.blit(pv.disp.image, (x, y))
