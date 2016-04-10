import math
from solid import *
from solid.utils import *

# General parameter of the sieves (mm)
hole_diam = 10
box_size = 190
box_thickness = 5
box_height = 40

# hole radius
hr = hole_diam / 2.

# hole spacing
hsp = hole_diam * 1.4

base = difference()(
    translate([-box_size/2 + box_thickness, -box_size/2 + box_thickness, -box_height/2.])(
        minkowski()(
            cube([box_size-2*box_thickness, box_size-2*box_thickness, box_height/2.]),
            cylinder(r=5, h=box_height/2.))),
    translate([0, 0, box_thickness])(
        cube([box_size - 2 * box_thickness,
              box_size - 2 * box_thickness,
              box_height], center=True)
    )
)

# sieve pile up
cw = box_size/2. - box_thickness*3/4.
bottom_guides = (translate([cw, cw,-box_height/2])(sphere(2)) +
                 translate([cw, -cw,-box_height/2])(sphere(2)) +
                 translate([-cw, cw,-box_height/2])(sphere(2)) +
                 translate([-cw, -cw,-box_height/2])(sphere(2)))
top_guides = (translate([cw, cw, box_height/2])(sphere(1.5)) +
              translate([cw, -cw, box_height/2])(sphere(1.5)) +
              translate([-cw, cw, box_height/2])(sphere(1.5)) +
              translate([-cw, -cw, box_height/2])(sphere(1.5)))

# odd lines holes
x_range = int(math.floor((box_size / 2. - box_thickness - hr) / hsp))
y_range = int(math.floor((box_size / 2. - box_thickness - hr) / hsp / 2))

l =[]
for i in range(-x_range, x_range + 1):
    for j in range(-y_range, y_range + 1):
        l.append(translate([i*hsp, j*hsp*2, 0])(
            cylinder(r=hr, h=100, center=True))

             )

# even lines holes
x_range = int(math.floor((box_size / 2. - box_thickness) / hsp))
y_range = int(math.floor((box_size / 2. - box_thickness) / hsp / 2))

l2 = []
for i in range(-x_range, x_range):
    for j in range(-y_range, y_range):
        l2.append(translate([(i + 1/2.)*hsp, (2*j + 1)*hsp, 0])(
                cylinder(r=hr, h=100, center=True))
        )

d = base - l - l2 - bottom_guides + top_guides

scad_render_to_file(d, 'sieve1.scad')
