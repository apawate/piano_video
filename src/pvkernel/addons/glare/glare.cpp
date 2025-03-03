//
//  Piano Video
//  A free piano visualizer.
//  Copyright Patrick Huang 2021
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.
//

#include <algorithm>
#include <cmath>
#include <iostream>
#include "../../utils.hpp"
#include "../../random.hpp"


/**
 * Render the glare on an image.
 * @param img Image.
 * @param width height: Image dimensions.
 * @param intensity Glare intensity factor.
 * @param radius Glare radius.
 * @param notes Array of notes to add glare to (0 is lowest note).
 * @param num_notes Number of notes.
 * @param x_start X pixel start of piano.
 * @param x_end X pixel end of piano.
 */
extern "C" void glare(UCH* img, const int width, const int height, CD intensity, CD radius,
        const UCH* notes, const UCH num_notes, CD x_start, CD x_end, CD jitter) {
    CD mid = height / 2.0;
    const UCH white[3] = {255, 255, 255};
    const int border = 25;

    for (UCH i = 0; i < num_notes; i++) {
        const UCH note = notes[i];
        CD x_pos = key_pos(x_start, x_end, note);
        CD curr_intensity = intensity - Random::uniform(0, jitter);

        for (int x = x_pos-radius-border; x < x_pos+radius+border; x++) {
            for (int y = mid-radius-border; y < mid+radius+border; y++) {
                CD dx = abs(x-x_pos), dy = abs(y-mid);
                CD dist = pythag(x-x_pos, y-mid);
                CD dist_fac = dist / radius;

                // Streaks
                CD angle = degrees(atan(dy/dx));
                CD angle_dist = std::min(abs(angle-23), abs(angle-54));
                CD angle_fac = dbounds(map_range(angle_dist, 0, 5, 0.96, 1));

                CD fac = dbounds(1 - (angle_fac*dist_fac));  // 0 = full white, 1 = no white
                CD real_fac = fac * curr_intensity;      // Account for intensity
                if (real_fac < 0)
                    std::cout << real_fac << std::endl;
                img_mixadd(img, width, x, y, real_fac, white);
            }
        }
    }
}
