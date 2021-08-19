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

.PHONY: help build dist docs ps

help:
	# Please see https://piano-video.rtfd.io for support.

build:
	cd ./src/pvkernel; \
	make;

dist:
	cd ./build; \
	python main.py;

docs:
	cd ./docs; \
	make html;

ps:   # pianosynth
	cd ./src/pianosynth; \
	make;
