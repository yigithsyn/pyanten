import sys

# setting path
sys.path.append('./src/')
from pyanten import Propagation

assert round(Propagation.farFieldDistance(9E9, 0.3), 3) == 5.404
assert round(Propagation.lineOfSight(10), 2)            == 11.29
assert round(Propagation.radioHorizon(10), 2)           == 13.03
assert round(Propagation.pathLoss(500, 11, 20, 0), 1)   == 87.3

