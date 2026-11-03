## Star-Formation-History
Investigating the integrated star formation histories (SFHs) of all GECKOS galaxies using the nGIST analysis pipeline.

# First Milestone: Understanding the data, stellar population models, and nGIST
Week 2 Goals
- Explore the different components of the project by creating a colour image from a single galaxy data cube (Y)
- Install nGIST (N)

Week 3 Goals
- Run the nGIST tutorial (N)

Week 4 Goals
- Plot stellar population spectra as a function of age and metallicity for the different SPS models
    - Plot frequency vs. wavelength for various MILES variables (vary age and/or metallicity) onto same graph (Y)
    - Plot frequency vs. wavelength for various SSP's (MILES, sMILES, XSL, alphaMC) with the same  age and metallicity (N)
- Run the nGIST tutorial (N)

Week 5 Goals
- Get nGIST running and do the tutorial (Y)
- Plot flux vs wavelength for different SSP's with the same age and metallicity (Y)

Week 7 Goals
- Run low metallicity alphamc at higher ages (Y)
- Try secondary alphamc file for better matching with miles (Y)
- Try plotting sMILES and xshooter (okay if variables don't match, just note them) (Y)
    - compare alphamc to xshooter due to their shared higher res (N)
    - Gausian smoothing? to fix different resolutions (N)
- Run new galaxy on nGIST? mess with Mapviewer (type in terminal, select folder) (N)

Week 8 Goals (send Jesse nGIST changes)
- xShooter
- Geckos ESO120 through nGIST
    - Min S/N = 5 (minimum signal to noise thst will be binned)
    - Target S/N = choose large enough S/N so that we only have one bin of the entire galaxy (to look at overall sfh)
        - turn off all modules when working out S/N number (from kin onwards)
        - use override=True
- Try IS1711? Run all the above again
    - For mapviewer, bottom left and bottom middle graphs (MassAge, Z/HAge)
- Contact Jesse if finish the list