from numpy import floor, ceil, mod

from pyanten.Measurement.NearField.Planar.samplingLength import samplingLength

def samplingCount(frequency, L):
  r""" Planar near-field antenna measurement sampling count according to frequency and desired minimum length

  Parameters
  ----------
  frequency : array_like [float]
              frequency of interest in Hertz [Hz]
  L         : array_like [float]
              desired minimum scan length [m]

  Returns
  -------
  Lm    : array_like [float]
          sampling start position [m]
  Lp    : array_like [float]
          sampling stop position [m] (equals to negative of Lp)
  N     : array_like [float]
          samplng count
  Delta : array_like [float]
          spatial samplng length [mm]

  Notes
  -----
  Calculation assumes a scanning region centered on the AUT.  

  Formula
  -------
  .. math::
      theta = \tan^{-1} \left \dfrac{L-a}{2d} \right
  """
  
  samplingLengthInmm = floor(samplingLength(frequency)*1E3)
  scanLengthInmm     = ceil(L*1E3)
  halfScanLengthInmm = scanLengthInmm/2 if mod(scanLengthInmm,2) ==0 else (scanLengthInmm+1)/2
  if mod(halfScanLengthInmm, samplingLengthInmm) > 0:
    halfScanLengthInmm = halfScanLengthInmm + (samplingLengthInmm-mod(halfScanLengthInmm, samplingLengthInmm))
  
  N  = 2*(halfScanLengthInmm/samplingLengthInmm)+1
  Lm = -halfScanLengthInmm
  Lp = +halfScanLengthInmm
  
  return [ Lm.tolist()/1E3, Lp.tolist()/1E3, N.astype('int').tolist(), samplingLengthInmm.astype('int').tolist() ] 