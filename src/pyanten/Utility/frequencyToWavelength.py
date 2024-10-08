from numpy import asarray
from scipy.constants import speed_of_light

def frequencyToWavelength(frequency):
  """ Converts frequency to wavelength

  Parameters
  ----------
  frequency : array_like [float]
      frequency in Hertz [Hz]

  Returns
  -------
  wavelength : array_like [float]
      wavelength in meters [m]
  """
  return (speed_of_light / asarray(frequency)).tolist()