from numpy import asarray, power

from pyanten.Utility.gammaToSwr import gammaToSwr

def gammaDbToSwr(gamma):
  """ Reflection coefficient (gamma) in decibels to voltage standing wave ratio (vswr) conversion

  Parameters
  ----------
  gamma : array_like [float]
      reflection coefficient (s11) [dB]

  Returns
  -------
  swr : array_like [float]
      standing wave ratio (swr)
  """
  gammaLin = power(10,asarray(gamma)/20) 
  return gammaToSwr(gammaLin)