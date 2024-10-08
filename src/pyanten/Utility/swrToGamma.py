from numpy import asarray

def swrToGamma(swr):
  """ Voltage standing wave ratio (vswr) to reflection coefficient (gamma) conversion

  Parameters
  ----------
  swr : array_like [float]
      standing wave ratio (swr)

  Returns
  -------
  gamma : array_like [float]
      reflection coefficient (s11)
  """
  return ((asarray(swr)-1)/(asarray(swr)+1)).tolist()