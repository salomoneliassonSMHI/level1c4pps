#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Adam.Dybbroe

# Author(s):

#   Adam.Dybbroe <adam.dybbroe@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Script to convert MERSI-2 level-1 to PPS level-1c format using Pytroll/Satpy
"""

import argparse
from level1c4pps.mersi22pps_lib import process_one_scene


if __name__ == "__main__":
    """ Create PPS-format level1c data
    From a list of MERSI-2 level-1 files create a NWCSAF/PPS formatet level1c file for pps.
    """
    parser = argparse.ArgumentParser(
        description=('Script to produce a PPS-level1c file for a MERSI-2 level-1 scene'))
    parser.add_argument('files', metavar='fileN', type=str, nargs='+',
                        help='List of MERSI-2 files to process')
    parser.add_argument('-o', '--out_dir', type=str, nargs='?',
                        required=False, default='.',
                        help="Output directory where to store the level1c file")

    options = parser.parse_args()
    process_one_scene(options.files, options.out_dir)
