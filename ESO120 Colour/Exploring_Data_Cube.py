from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb

#hdul = fits.open('ESO120-016_DATACUBE_iDR1.fits')
#hdul.info()

# opens the fits file, pulls out the appropriate data, closes the file
with fits.open('c:/Users/briaj/OneDrive/Desktop/UNSW/Year 3 (2026)/PHYS4200 (Research Project)/Star-Formation-History/Data/ESO120-016_DATACUBE_iDR1.fits') as hdul:
    data = hdul['DATA'].data   # actual data, shape (wavelength, y, x)
    dq= hdul['DQ'].data        # quality of data, if anything other than 0 its no good
    hdr = hdul['DATA'].header  # headers of the actual data

# translating the raw data of the wavelength axis to actual wavelengths for clearer and easier use
n_wave = data.shape[0]                       # the spectral slices
crval3 = hdr['CRVAL3']                       # translating to wavelength using the refrences wavelength in the data
crpix3 = hdr['CRPIX3']                       # same with the refrence pixal
cdelt3 = hdr.get('CD3_3', hdr.get('CDELT3')) # getting the wavelength step per pixal (tries finding this value under name 'CD3_3', and if fails looks for 'CDELT3')

wave = crval3 + (np.arange(n_wave) + 1 - crpix3) * cdelt3   # standard formula for converting data into wavelength

# creating new data cube where all the bad data (data_quality value isn't 0) is removed
cube = np.where(dq==0, data, np.nan)  # np.where(condition, x, y) --> when condition is true, gives x, when false gives y

# defines which wavelengths fall under which colour
blue_range  = (4800, 6100)
green_range = (6100, 7500)
red_range   = (7500, 9300)

# creates the mask for each band of colour as only a certain wavelength range
def band_image(cube, wave, wmin, wmax):
    mask = (wave >= wmin) & (wave <= wmax) 
    return np.nansum(cube[mask, :, :], axis=0)

# defining the colour bands
b_img = band_image(cube, wave, *blue_range)
g_img = band_image(cube, wave, *green_range)
r_img = band_image(cube, wave, *red_range)

# identifying the background noise
sky = (slice(150, 250), slice(20, 60)) # defines an area in the image that is just sky to use as a baseline
r_img = r_img - np.median(r_img[sky])  # subtracts the sky background from each channel: finds the
g_img = g_img - np.median(g_img[sky])  #    median of each colour in the sky patch to subtract  
b_img = b_img - np.median(b_img[sky])  #    from the rest of the image
total = r_img + g_img + b_img          # this is the total background noise of the chosen empty patch
noise = np.std(total[sky])             # the background noise, the size of the typical background fluctuation

# removing the background noise
scale = np.percentile(total[:, 180:260], 99)   # finds nearly (99th percentile) the brightest refrence in the galaxy region
rgb = make_lupton_rgb(r_img/scale, g_img/scale, b_img/scale, stretch=0.5, Q=8) # builds the colour image
#   --> dividing by the scale means the brightness values are mostly between 0 and 1 
rgb[total < 3 * noise] = 0 # ensures any values below 3 times the background noise are 0
# *plot a histagram to look at the noise
# * play with line 53 --> look at background noise, can you emphasise certain features?

# making the figure
plt.figure(figsize=(8, 8))
plt.imshow(rgb, origin='lower')
plt.axis('off')
plt.title('ESO 120-016 — color composite')
plt.tight_layout()
plt.savefig('ESO120-016_color.png', dpi=200)
plt.show()

