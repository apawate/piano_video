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

import cv2


def compute_crop_points(settings):
    (x1, y1), (x2, y2), height = settings["piano.video_crop"]
    slope = (y2-y1) / (x2-x1)
    x3, y3 = (x1-height*slope if slope != 0 else x1), y1+height
    x4, y4 = x3 + (x2-x1), y3 + (y2-y1)

    settings["piano.video_crop_x1"] = x1
    settings["piano.video_crop_y1"] = y1
    settings["piano.video_crop_x2"] = x2
    settings["piano.video_crop_y2"] = y2
    settings["piano.video_crop_x3"] = x3
    settings["piano.video_crop_y3"] = y3
    settings["piano.video_crop_x4"] = x4
    settings["piano.video_crop_y4"] = y4
