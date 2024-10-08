from numpy import asarray, tan, radians

def scanLength(a, d, theta):
  r""" Required length of the scan for desired angle-of-view in planar near-field antenna measurements

  Parameters
  ----------
  a     : array_like [float]
          antenna cross-section length
  d     : array_like [float]
          seperation distance between antenna and probe
  theta : array_like [float]
          desired pattern view angle along one side [deg]

  Notes
  -----
  Calculation assumes a scanning region centered on the AUT.
  Input distances are unitless so output is the same quantity of inputs.

  References
  ----------
  .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 135, Equation 99.
  .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.6, Page 28, Equation 27.

  Formula
  -------
  .. math::
      L = 2d \cdot \tan\theta + a
  """
  
  L = 2*asarray(d) * tan(radians(theta)) + asarray(a)
  return L.tolist()