from numpy import asarray, atan2, rad2deg


def angleOfView(a, d, L):
  r""" Reliable far-field angle-of-view in planar near-field antenna measurements

  Parameters
  ----------
  a : array_like [float]
      antenna cross-section length
  d : array_like [float]
      seperation distance between antenna and probe
  L : array_like [float]
      scan length of region

  Notes
  -----
  Calculation assumes a scanning region centered on the AUT.  
  Input distances are unitless but should in same quantity

  References
  ----------
  .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 135, Equation 99.
  .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.6, Page 28, Equation 27.

  Formula
  -------
  .. math::
      theta = \tan^{-1} \left \dfrac{L-a}{2d} \right
  """

  theta = rad2deg(atan2(asarray(L)-asarray(a), 2*asarray(d)))
  return theta.tolist()