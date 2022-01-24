#!/usr/bin/env python3

from gcode_utils import GcodeWriter
from path_primitives import CirclePath

gw = GcodeWriter("iso_path.nc")
gw.set_absolute_motion()
gw.set_units("mm")
gw.comment("goto safe place")
gw.goto(x=0, y=0, z=15)

gw.comment("cut circle")
cp = CirclePath(gcode_writer=gw, center=[0,0], r=args.radius, f=args.cut_speed, bit_width=0.762, z=-0.05)
cp.execute()

gw.comment("when finished go back to x0y0zsafe")
gw.goto(x=0, y=0, z=15)
gw.set_spindle_speed(0)
gw.end_program()
