# sieve3d

## Summary

Script to generate variable size sieves (for 3D printing) to help with Lego sorting. Details at: https://www.brickodyssey.com/3d-printing-lego-sieves/

## Usage

This is using SolidPython to generate the scad file. So you need to install that first: follow the instructions at https://github.com/SolidCode/SolidPython

Once this is done, edit the script to change the `hole_diam` and the `sep` param to a suitable value (several sieves of different size are probably needed). Then, run as

```
python generate.py
```

Then use OpenSCAD (for example, other programs will work as well) to convert this to a stl suitable for printing. Alternatively, you can download the stl directly from http://www.thingiverse.com/brickodyssey/designs