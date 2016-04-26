import math
from solid import *
from solid.utils import *

# General parameter of the sieves (mm)

# holes diameter
hole_diam = 18
# distance between holes centers, in hole diameter unit (a value of 1 would have
# the holes touching). Some values that work well
# 18 mm : 1.25
# 14 mm : 1.23
# 10 mm : 1.28
sep = 1.25

# other parameters that will probably not change
output_file = 'sieve_%d.scad' % hole_diam
box_size = 190
box_thickness = 5
box_height = 40

# hole radius
hr = hole_diam / 2.

# hole spacing x
hspx = hole_diam * sep
# hole spacing y
hspy = hole_diam * sep * sqrt(3.)/2.

base = difference()(
    translate([-box_size/2. + box_thickness, -box_size/2. + box_thickness, -box_height/2.])(
        minkowski()(
            cube([box_size-2.*box_thickness, box_size-2.*box_thickness, box_height/2.]),
            cylinder(r=5, h=box_height/2.))),
    translate([0, 0, box_thickness])(
        cube([box_size - 2. * box_thickness,
              box_size - 2. * box_thickness,
              box_height], center=True)
    )
)

# sieve pile up
cw = box_size/2. - box_thickness*3/4.
bottom_guides = (translate([cw, cw,-box_height/2.])(sphere(2.)) +
                 translate([cw, -cw,-box_height/2.])(sphere(2.)) +
                 translate([-cw, cw,-box_height/2.])(sphere(2.)) +
                 translate([-cw, -cw,-box_height/2.])(sphere(2.)))
top_guides = (translate([cw, cw, box_height/2.])(sphere(1.5)) +
              translate([cw, -cw, box_height/2.])(sphere(1.5)) +
              translate([-cw, cw, box_height/2.])(sphere(1.5)) +
              translate([-cw, -cw, box_height/2.])(sphere(1.5)))

# odd lines holes
x_range = int(math.floor((box_size / 2. - box_thickness - hr) / hspx))
y_range = int(math.floor((box_size / 2. - box_thickness - hr) / hspy / 2.))

l =[]
for i in range(-x_range, x_range + 1):
    for j in range(-y_range, y_range + 1):
        l.append(translate([i*hspx, j*hspy*2., 0])(
            cylinder(r=hr, h=100, center=True))
        )

# even lines holes
x_range = int(math.floor((box_size / 2. - box_thickness) / hspx))
y_range = int(math.floor((box_size / 2. - box_thickness) / hspy / 2.))

l2 = []
for i in range(-x_range, x_range):
    for j in range(-y_range, y_range):
        l2.append(translate([(i + 1/2.)*hspx, (2.*j + 1)*hspy, 0])(
                cylinder(r=hr, h=100, center=True))
        )

d = base - l - l2 - bottom_guides + top_guides

scad_render_to_file(d, output_file)
