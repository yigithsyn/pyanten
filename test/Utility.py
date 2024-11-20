import sys
import pytest

sys.path.append('./src')
from pyanten import Utility


assert Utility.frequencyToWavelength(1E6)        == 299.792458
assert Utility.wavelengthToFrequency(299.792458) == 1E6

assert round(Utility.gammaToSwr(0.333),2) == 2.00
assert round(Utility.swrToGamma(2.00),2)  == 0.33

assert round(Utility.gammaDbToSwr(-9.540),2) == 2.00
assert round(Utility.swrToGammaDb(2.00),2)   == -9.54

assert round(Utility.gammaDbToReflectedPowerPercentage(-9.5),1) == 11.2