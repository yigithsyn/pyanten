from numpy import asarray

def gammaToSwr(gamma):
  """ Reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion

  Parameters
  ----------
  gamma : array_like [float]
      reflection coefficient (s11)

  Returns
  -------
  swr : array_like [float]
      standing wave ratio (swr)
  """
  return (1+asarray(gamma))/(1-asarray(gamma)).tolist()