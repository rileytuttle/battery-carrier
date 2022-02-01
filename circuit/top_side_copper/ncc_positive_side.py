#!/usr/bin/env python3

import sys
import os
gcode_utils_path = os.path.join(os.environ['HOME'], "gcode_tools")
sys.path.append(gcode_utils_path)

from gcode_utils import GcodeWriter
from path_primitives import ArcPath, CirclePath

gw = GcodeWriter("output_files/ncc_positive_side.nc")
gw.set_absolute_motion()
gw.set_units("mm")

gw.comment("goto safe place")
gw.goto(x=0, y=0, z=3)

inner_diam = 13
inner_radius = inner_diam / 2.0
outer_diam = 23
feedrate = 30
bit_width = 0.762
plunge_depth = -0.07

outer_radius = outer_diam / 2.0
gw.comment(f"cut outer full circle and mill outwards from radius={inner_radius} to radius={outer_radius}mm")
overlap = 0.1 # 10% overlap
current_radius = inner_radius
while current_radius <= outer_radius:
    gw.comment(f"mill at {current_radius}mm radius")
    outer_cp = CirclePath(gcode_writer=gw, center=[0,0], r=current_radius, f=feedrate, bit_width=bit_width, pz=plunge_depth)
    outer_cp.execute()
    current_radius += (bit_width * (1 - overlap))

gw.comment(f"finished milling at current_radius = {current_radius}mm")
gw.comment("when finished go back to x0y0zsafe")
gw.goto(x=0, y=0, z=15)
gw.set_spindle_speed(0)
gw.end_program()
