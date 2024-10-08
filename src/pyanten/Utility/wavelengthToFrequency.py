from pyanten.Utility.frequencyToWavelength import frequencyToWavelength

def wavelengthToFrequency(wavelength):
  """ Converts frequency to wavelength

  Parameters
  ----------
  wavelength : array_like [float]
      wavelength in meters [m]

  Returns
  -------
  frequency : array_like [float]
      frequency in Hertz [Hz]
  """
  return frequencyToWavelength(wavelength)