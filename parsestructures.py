from pprint import pprint
import numpy as np
from ase import Atoms
from ase.io import write


data = open("structures.txt").read()
ds1 = data.split("#")
ds2 = [x.strip().split('\n')[1:] for x in ds1[1:]]
ds3 = [[y.split() for y in x] for x in ds2 if len(x) > 0]
ds4 = [[(x[-1].title(), [float(z) for z in x[:-1]]) for x in y] for y in ds3]
names = [[x[0] for x in y] for y in ds4]
positions = [np.array([x[1:][0] for x in y]) for y in ds4]

atoms_list = []
for name, position in zip(names, positions, strict=True):
    atoms_list.append(Atoms(name, positions=position))

write("structures.extxyz", atoms_list)