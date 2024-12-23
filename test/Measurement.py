import sys
import pytest

# setting path
sys.path.append('./src')
from pyanten import Measurement

assert round(Measurement.NearField.seperationDistance(10E9), 3) == 0.150

assert round(Measurement.NearField.Planar.samplingLength(3E9), 3)        == 0.050
assert round(Measurement.NearField.Planar.scanLength(20, 10, 60), 2)     == 54.64
assert Measurement.NearField.Planar.samplingParameters(3E9, 1)                == (-0.539, +0.539, 23, 49)
assert round(Measurement.NearField.Planar.angleOfView(20, 10, 54.64), 2) == 60.00

assert round(Measurement.NearField.Spherical.maximumRadiusExtent(3,4,12), 2) == 13.00

