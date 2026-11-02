## Understanding the fits file
# HDU[0]: essentially the x-axis values, 37150 of them
# HDU[1]: the actual data, a 2D (3360, 37150) array, with 3360 spectra, each with 37150 flux values 
#           (ie. one spectra of the 3360 is one look at the general population for a set age and metallicity)
# HDU[2]: 3360 rows and 3 columns (logt, feh, afe), essentially our lookup, first row values correspond to the 
#           first spectra in HDU[1]
# Metallicity values for alphaMC: −1.5, −1.25, −1.0, −0.75, −0.5, −0.25, 0.0, +0.25

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

with fits.open('Data/alphaMC_Data.fits') as hdul:
    wave = np.array(hdul[0].data, dtype=float)
    tab  = hdul[2].data

    logt = np.array(tab['logt'])
    feh  = np.array(tab['feh'])
    afe  = np.array(tab['afe'])

    age_gyr = 10**logt / 1e9 # 10** cancels the log of the age, /1e9 converts to Gyrs

    # the values we want to find
    our_ages = [0.05, 0.25, 1]   # Gyr
    our_feh = -0.25
    our_afe = 0

    c = 2.99792458e18   # speed of light in Å/s

    m = (wave > 3540) & (wave < 7410) # MILES wavelength range

    fig, ax = plt.subplots(figsize=(10, 5.5))

    for our_age in our_ages:
        d = np.log10(age_gyr / our_age)**2 + (feh - our_feh)**2 + (afe - our_afe)**2 # asks which row is closest to the values we want to find
        i = np.argmin(d) # finds the row with the smallest distance, ie. the closest model
        spec = np.array(hdul[1].data[i], dtype=float) # chooses the correct row of spectra as selected above
        spec_lam = spec * c / wave**2       # converts flux units from per-unit-frequency to per-unit-wavelength, to match the MILES convention

        print(i, age_gyr[i], feh[i], afe[i]) # prints actual values chosen through the rounding 

        ax.plot(wave[m], spec_lam[m], lw=0.8, label=f'alphaMC: T={age_gyr[i]:.2f}')   # the ONLY plot call



## Plotting MILES with Metallicity (Z) = -0.25
with fits.open('nGIST Repos/ngist_supplementary_public/ngistTutorial/spectralTemplates/MILES/Mch1.30Zm0.25T00.0500_iTp0.00_baseFe_linear_FWHM_2.51.fits') as hdul_m025_005:
    #hdul.info()
    #print(hdul[0].header)
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



ax.plot(wave_m025_005, flux_m025_005, label="MILES: T=0.05")
ax.plot(wave_m025_025, flux_m025_025, label="MILES: T=0.25")
ax.plot(wave_m025_100, flux_m025_100, label="MILES: T=1.00")


ax.set_xlabel('Wavelength')
ax.set_ylabel('Flux [L$_\\odot$/Å/M$_\\odot$]')
ax.set_title("SSP's at Metallicity Z=-0.25")
ax.legend()
plt.show()

hdul.close()
hdul_m025_005.close()
hdul_m025_025.close()
hdul_m025_100.close()
