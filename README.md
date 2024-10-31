# PyAnten

Antenna Toolkit

## Installation

```shell
git clone https://github.com/atamlab/pyanten
cd pyanten
pip install . # or python setup.py
```

## Table of Modules and Functions

| Module      | Sub Module (Level1) | Sub Module (Level2) | Functinos                                                                                        |
| ----------- | ------------------- | ------------------- | ------------------------------------------------------------------------------------------------ |
| Utility     |                     |                     | frequencyToWavelength, gammaDbToSwr, gammaToSwr, swrToGamma, swrToGammaDb, wavelengthToFrequency |
| Propagation |                     |                     | farfFieldDistance, lineOfSight, pathLoss, radioHorizon,                                          |
| Measurement | NearField           |                     | minimumRange,                                                                                    |
| Measurement | NearField           | Planar              | angleOfView, samplingCount, samplingLength, scanLength,                                          |
| Measurement | NearField           | Spherical           | maximumRadiusExtent,                                                                             |
| Array       |                     |                     | amplitudeTaper,                                                                                  |

## References

[1] [A Python MoM antenna simulator](https://www.linkedin.com/pulse/python-mom-antenna-simulator-t-q-khai-nguyen/)
