from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

## Plotting MILES with Metallicity (Z) = 0.40
with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T00.0500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_005:
    flux_005 = hdul_005[0].data
    h = hdul_005[0].header
wave_005 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T00.1000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_010:
    flux_010 = hdul_010[0].data
    h = hdul_010[0].header
wave_010 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T00.1500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_015:
    flux_015 = hdul_015[0].data
    h = hdul_015[0].header
wave_015 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T00.2500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_025:
    flux_025 = hdul_025[0].data
    h = hdul_025[0].header
wave_025 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T00.5000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_050:
    flux_050 = hdul_050[0].data
    h = hdul_050[0].header
wave_050 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T01.0000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_100:
    flux_100 = hdul_100[0].data
    h = hdul_100[0].header
wave_100 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T02.0000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_200:
    flux_200 = hdul_200[0].data
    h = hdul_200[0].header
wave_200 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zp0.40T03.0000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_300:
    flux_300 = hdul_300[0].data
    h = hdul_300[0].header
wave_300 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))


## The Plotting
fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(wave_005, flux_005, label="T=0.05")
axes[0, 0].plot(wave_010, flux_010, label="T=0.10")
axes[0, 0].plot(wave_015, flux_015, label="T=0.15")
axes[0, 0].plot(wave_025, flux_025, label="T=0.25")
axes[0, 0].plot(wave_050, flux_050, label="T=0.50")
axes[0, 0].plot(wave_100, flux_100, label="T=1.00")
axes[0, 0].plot(wave_200, flux_200, label="T=2.00")
axes[0, 0].plot(wave_300, flux_300, label="T=3.00")
axes[0, 0].title("SSP's at Metallicity Z=0.40")
axes[0, 0].legend()


plt.xlabel("Wavelength")
plt.ylabel("Flux")

plt.tight_layout()
plt.show()

hdul_005.close()
hdul_010.close()
hdul_015.close()
hdul_025.close()
hdul_050.close()
hdul_100.close()
hdul_200.close()
hdul_300.close()