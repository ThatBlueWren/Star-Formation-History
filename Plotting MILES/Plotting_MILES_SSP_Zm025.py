# MILES Files: ngist_supplementary_public > ngistTutorial > spectralTemplates > MILES
# Note: File notation
#   Z p/m 0.00 -->  Metallicity pos or neg
#   T 0.00     -->  Age in Gyrs

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

## Plotting MILES with Metallicity (Z) = -0.25
with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.0500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_005:
    #hdul.info()
    #print(hdul[0].header)
    flux_m025_005 = hdul_m025_005[0].data
    h = hdul_m025_005[0].header
wave_m025_005 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.1000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_010:
    flux_m025_010 = hdul_m025_010[0].data
    h = hdul_m025_010[0].header
wave_m025_010 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.1500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_015:
    flux_m025_015 = hdul_m025_015[0].data
    h = hdul_m025_015[0].header
wave_m025_015 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.2500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_025:
    flux_m025_025 = hdul_m025_025[0].data
    h = hdul_m025_025[0].header
wave_m025_025 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_050:
    flux_m025_050 = hdul_m025_050[0].data
    h = hdul_m025_050[0].header
wave_m025_050 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T01.0000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_100:
    flux_m025_100 = hdul_m025_100[0].data
    h = hdul_m025_100[0].header
wave_m025_100 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

plt.plot(wave_m025_005, flux_m025_005, label="T=0.05")
plt.plot(wave_m025_010, flux_m025_010, label="T=0.10")
plt.plot(wave_m025_015, flux_m025_015, label="T=0.15")
plt.plot(wave_m025_025, flux_m025_025, label="T=0.25")
plt.plot(wave_m025_050, flux_m025_050, label="T=0.50")
plt.plot(wave_m025_100, flux_m025_100, label="T=1.00")
plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.title("SSP's at Metallicity Z=-0.25")
plt.legend()
plt.show()

hdul_m025_005.close()
hdul_m025_010.close()
hdul_m025_015.close()
hdul_m025_025.close()
hdul_m025_050.close()
hdul_m025_100.close()