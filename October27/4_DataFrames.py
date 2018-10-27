import numpy as np
import pandas as pd
from numpy.random import randn

outside = 'G1 G1 G1 G2 G2 G2'.split()
print(outside)
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
print(hier_index)
