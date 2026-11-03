import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Plotting xShooter at M/H = -0.2
with fits.open('Data/xShooter_MHm02_logT77.fits') as XSL_logT77:
    flux_XSL_logT77 = XSL_logT77[0].data
    h = XSL_logT77[0].header
wave_XSL_logT77 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))
wave_XSL_logT77 = 10 * 10**wave_XSL_logT77          # log10(nm) -> Angstrom
real_age_logT77 = 10**(float(h["LOGAGE"]) - 9)


with fits.open('Data/xShooter_MHm02_logT84.fits') as XSL_logT84:
    flux_XSL_logT84 = XSL_logT84[0].data
    h = XSL_logT84[0].header
wave_XSL_logT84 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))
wave_XSL_logT84 = 10 * 10**wave_XSL_logT84
real_age_logT84 = 10**(float(h["LOGAGE"]) - 9)


with fits.open('Data/xShooter_MHm02_logT90.fits') as XSL_logT90:
    flux_XSL_logT90 = XSL_logT90[0].data
    h = XSL_logT90[0].header
wave_XSL_logT90 = h["CRVAL1"] + h["CDELT1"] * (np.arange(h["NAXIS1"]) - (h["CRPIX1"] - 1))
wave_XSL_logT90 = 10 * 10**wave_XSL_logT90
real_age_logT90 = 10**(float(h["LOGAGE"]) - 9)


## Plotting alphaMC at metallicity -0.25
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


mask = (wave_XSL_logT77 > 3500) & (wave_XSL_logT77 < 7400)

## SCALE FOR XSL IS WAY OFF --> don't know the conversion to match alphaMC\
#     #convert fluxes from F [erg cm s Å] to  Lsun/ Lsun Msun Å
    # first check if templates are kroupa or salpeter
    # if "Kroupa" in ssp_models[0]:
    #    C_flux =  (4* np.pi * (3.08567758128e19)**2) / (3.828e33) / (0.562)    

ax.plot(wave_XSL_logT77[mask], flux_XSL_logT77[mask], label=f"XSL: T={real_age_logT77:.2f}")
ax.plot(wave_XSL_logT84[mask], flux_XSL_logT84[mask], label=f"XSL: T={real_age_logT84:.2f}")
ax.plot(wave_XSL_logT90[mask], flux_XSL_logT90[mask], label=f"XSL: T={real_age_logT90:.2f}")


ax.set_xlabel('Wavelength [Å]')
ax.set_ylabel('Flux [L$_\\odot$/Å/M$_\\odot$]') ## for alphaMC
ax.set_title("SSP's at Metallicity Z=-0.2 (Z=-0.25 for alphaMC)")
ax.legend()
plt.show()


XSL_logT77.close()
XSL_logT84.close()
XSL_logT90.close()