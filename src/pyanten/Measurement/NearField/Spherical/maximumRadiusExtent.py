from numpy import square, sqrt
from pyanten.Utility import frequencyToWavelength

def maximumRadiusExtent(dx, dy, dz):
  r""" Calculates maximum radial extend (MRE) of the antenna for spherical near-field (SNF) measurements

  Parameters
  ----------
  dx : array_like [float]
       max displacement from rotation center along x-axis
  dy : array_like [float]
       max displacement from rotation center along y-axis
  dz : array_like [float]
       max displacement from rotation center along z-axis

  Returns
  -------
  mre : array_like [float]
        maximum radius extent

  Notes
  -----
  Calculation is unitless so output is the same quantity of inputs.

  Formula
  -------
  .. math::
      mre &= \sqrt{dx^2+dy^2+dz^2}
  """
  
  return sqrt(square(dx) + square(dy) + square(dz)).tolist()
