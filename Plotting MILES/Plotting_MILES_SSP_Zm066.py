# MILES Files: ngist_supplementary_public > ngistTutorial > spectralTemplates > MILES
# Note: File notation
#   Z p/m 0.00 -->  Metallicity pos or neg
#   T 0.00     -->  Age in Gyrs

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

## Plotting MILES with Metallicity (Z) = -0.66
with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T00.0500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_005:
    flux_005 = hdul_005[0].data
    h = hdul_005[0].header
wave_005 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T00.1000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_010:
    flux_010 = hdul_010[0].data
    h = hdul_010[0].header
wave_010 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T00.1500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_015:
    flux_015 = hdul_015[0].data
    h = hdul_015[0].header
wave_015 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T00.2500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_025:
    flux_025 = hdul_025[0].data
    h = hdul_025[0].header
wave_025 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_050:
    flux_050 = hdul_050[0].data
    h = hdul_050[0].header
wave_050 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.66T01.0000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_100:
    flux_100 = hdul_100[0].data
    h = hdul_100[0].header
wave_100 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

plt.plot(wave_005, flux_005, label="T=0.05")
plt.plot(wave_010, flux_010, label="T=0.10")
plt.plot(wave_015, flux_015, label="T=0.15")
plt.plot(wave_025, flux_025, label="T=0.25")
plt.plot(wave_050, flux_050, label="T=0.50")
plt.plot(wave_100, flux_100, label="T=1.00")
plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.title("SSP's at Metallicity Z=-0.66")
plt.legend()
plt.show()

hdul_005.close()
hdul_010.close()
hdul_015.close()
hdul_025.close()
hdul_050.close()
hdul_100.close()