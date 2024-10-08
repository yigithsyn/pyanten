from numpy import log10

from pyanten.Utility.swrToGamma import swrToGamma

def swrToGammaDb(swr):
  """ Voltage standing wave ratio (vswr) to reflection coefficient (gamma) in decibel conversion

  Parameters
  ----------
  swr : array_like [float]
      standing wave ratio (swr)

  Returns
  -------
  gamma : array_like [float]
      reflection coefficient (s11) [dB]
  """
  return (20*log10(swrToGamma(swr))).tolist()