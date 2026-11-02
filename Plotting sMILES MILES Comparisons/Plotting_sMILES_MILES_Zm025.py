
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

## Plotting MILES with Metallicity (Z) = -0.25
with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.0500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_005:
    flux_m025_005 = hdul_m025_005[0].data
    h = hdul_m025_005[0].header
wave_m025_005 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.2500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_025:
    flux_m025_025 = hdul_m025_025[0].data
    h = hdul_m025_025[0].header
wave_m025_025 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T01.0000_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_100:
    flux_m025_100 = hdul_m025_100[0].data
    h = hdul_m025_100[0].header
wave_m025_100 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

## Plotting sMILES with metallicity (Z) = -0.25
with fits.open('Data/sMILES_aFe0_Zm025_T005.fits') as sMILES_005:
    sMILES_flux_005 = sMILES_005[0].data
    h = sMILES_005[0].header
sMILES_wave_005 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('Data/sMILES_aFe0_Zm025_T025.fits') as sMILES_025:
    sMILES_flux_025 = sMILES_025[0].data
    h = sMILES_025[0].header
sMILES_wave_025 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))

with fits.open('Data/sMILES_aFe0_Zm025_T100.fits') as sMILES_100:
    sMILES_flux_100 = sMILES_100[0].data
    h = sMILES_100[0].header
sMILES_wave_100 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))


fig, ax = plt.subplots(figsize=(10, 5.5))

ax.plot(wave_m025_005, flux_m025_005, label="MILES: T=0.05")
ax.plot(wave_m025_025, flux_m025_025, label="MILES: T=0.25")
ax.plot(wave_m025_100, flux_m025_100, label="MILES: T=1.00")

ax.plot(sMILES_wave_005, sMILES_flux_005, label="sMILES: T=0.05")
ax.plot(sMILES_wave_025, sMILES_flux_025, label="sMILES: T=0.25")
ax.plot(sMILES_wave_100, sMILES_flux_100, label="sMILES: T=1.00")


ax.set_xlabel('Wavelength')
ax.set_ylabel('Flux [L$_\\odot$/Å/M$_\\odot$]')
ax.set_title("SSP's at Metallicity Z=-0.25")
ax.legend()
plt.show()

hdul_m025_005.close()
hdul_m025_025.close()
hdul_m025_100.close()
sMILES_005.close()
sMILES_025.close()
sMILES_100.close()