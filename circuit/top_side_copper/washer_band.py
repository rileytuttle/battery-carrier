#!/usr/bin/env python3

import sys
import os
gcode_utils_path = os.path.join(os.environ['HOME'], "gcode_tools")
sys.path.append(gcode_utils_path)

from gcode_utils import GcodeWriter
from path_primitives import ArcPath, CirclePath

gw = GcodeWriter("output_files/washer_band_full_mill.nc")
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
gw.comment(f"cut inner left half circle {inner_radius}mm radius")
gw.set_safe_height(2)
inner_lap = ArcPath(gcode_writer=gw, center=[0,0], r=inner_radius, f=feedrate, bit_width=bit_width, pz=plunge_depth, start_point=[-1.870597203368, -5.8260644609], end_point=[-1.870597203368, 5.8260644609])
inner_lap.execute()
gw.safe_z()

gw.comment("cut inner right half circle")
inner_rap = ArcPath(gcode_writer=gw, center=[0,0], r=inner_radius, f=feedrate, bit_width=bit_width, pz=plunge_depth, start_point=[1.870597203368, 5.8260644609], end_point=[1.870597203368, -5.8260644609])
inner_rap.execute()
gw.safe_z()

outer_radius = outer_diam / 2.0
gw.comment(f"cut outer full circle and mill outwards from radius={outer_radius}mm")
full_diam = 35.0
overlap = 0.1 # 10% overlap
start_radius = outer_radius
end_radius = outer_radius + (bit_width * (1.0-overlap))
middle_radius = (end_radius + start_radius) / 2.0

gw.comment(f"mill at {start_radius}mm radius")
outer_cp = CirclePath(gcode_writer=gw, center=[0,0], r=start_radius, f=feedrate, bit_width=bit_width, pz=plunge_depth)
outer_cp.execute()

current_radius = outer_radius + ((bit_width/2) * (1 - overlap))
gw.comment(f"mill at {middle_radius}mm radius")
outer_cp = CirclePath(gcode_writer=gw, center=[0,0], r=middle_radius, f=feedrate, bit_width=bit_width, pz=plunge_depth)
outer_cp.execute()

current_radius = outer_radius + (bit_width * (1 - overlap))
gw.comment(f"mill at {end_radius}mm radius")
outer_cp = CirclePath(gcode_writer=gw, center=[0,0], r=end_radius, f=feedrate, bit_width=bit_width, pz=plunge_depth)
outer_cp.execute()

gw.comment(f"finished milling at current_radius = {end_radius}mm")
gw.comment("when finished go back to x0y0zsafe")
gw.goto(x=0, y=0, z=15)
gw.set_spindle_speed(0)
gw.end_program()
