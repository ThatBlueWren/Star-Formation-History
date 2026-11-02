# MILES Files: ngist_supplementary_public > ngistTutorial > spectralTemplates > MILES
# Note: File notation
#   Z p/m 0.00 -->  Metallicity pos or neg
#   T 0.00     -->  Age in Gyrs

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

## Plotting MILES with Age (T) = 0.50
with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025:
    flux_m025 = hdul_m025[0].data
    h = hdul_m025[0].header
wave_m025 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m066:
    flux_m066 = hdul_m066[0].data
    h = hdul_m066[0].header
wave_m066 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm1.26T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m126:
    flux_m126 = hdul_m126[0].data
    h = hdul_m126[0].header
wave_m126 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm1.79T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m179:
    flux_m179 = hdul_m179[0].data
    h = hdul_m179[0].header
wave_m179 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.15T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_p015:
    flux_p015 = hdul_p015[0].data
    h = hdul_p015[0].header
wave_p015 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_p040:
    flux_p040 = hdul_p040[0].data
    h = hdul_p040[0].header
wave_p040 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

plt.plot(wave_m025, flux_m025, label="Z=-0.25", alpha=0.8, lw=1)
plt.plot(wave_m066, flux_m066, label="Z=-0.66", alpha=0.8, lw=1)
plt.plot(wave_m126, flux_m126, label="Z=-1.26", alpha=0.8, lw=1)
plt.plot(wave_m179, flux_m179, label="Z=-1.79", alpha=0.8, lw=1)
plt.plot(wave_p015, flux_p015, label="Z=0.15", alpha=0.8, lw=1)
plt.plot(wave_p040, flux_p040, label="Z=0.40", alpha=0.8, lw=1)
plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.title("SSP's at Age T=0.50")
plt.legend()
plt.show()

hdul_m025.close()
hdul_m066.close()
hdul_m126.close()
hdul_m179.close()
hdul_p015.close()
hdul_p040.close()