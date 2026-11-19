import os
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from astropy.io import fits

# ---------------- Settings ----------------
RUN_ID = "ESO120-016_iDR1_SN50_2.5_LW_4750-8900_singlebin"
OUTPUT = "13_ESO120-016"

runs = {
    "MILES":   f"results/{OUTPUT}/{RUN_ID}_MILES/{RUN_ID}_MILES",
    "alphaMC": f"results/{OUTPUT}/{RUN_ID}_alphaMC/{RUN_ID}_alphaMC",
    "XSL":     f"results/{OUTPUT}/{RUN_ID}_XSL/{RUN_ID}_XSL",
}
bin_id        = 0      # row in the WEIGHTS table (single bin, so 0)
outdir        = "SFH Comparison Graphs/ESO120-016"   # folder the images are saved in (created if missing)
alpha_sel     = None   # None = sum over all [alpha/Fe]; or a number, e.g. 0.0, for one slice
shared_scales = True   # True: same axis ranges and colour scale in all three images
                       # False: each image is scaled to its own data
# ------------------------------------------


def load_run(base, bin_id=0):
    with fits.open(base + "_sfh_weights.fits") as f:
        w = f["WEIGHTS"].data["WEIGHTS"][bin_id].astype(float)
        g = f["GRID"].data
        names = g.names
        print(base.split("/")[-1], "GRID columns:", names)

        agecol = next(n for n in names if "AGE" in n.upper())
        metcol = next((n for n in names if n.upper() in ("METAL", "MET", "MH", "ZH", "FEH")), None)
        if metcol is None:   # fallback: any column containing MET, or Z
            metcol = next((n for n in names if "MET" in n.upper() or n.upper().startswith("Z")), None)
        if metcol is None:
            raise KeyError(f"No metallicity column found in GRID columns: {names}")
        alpcol = next((n for n in names if "ALPHA" in n.upper()), None)

        age = g[agecol].astype(float)
        if "LOG" in agecol.upper() or age.min() < 0:
            age = 10 ** age
        if age.max() > 1e3:           # years -> Gyr
            age = age / 1e9
        metal = g[metcol].astype(float)
        alpha = g[alpcol].astype(float) if alpcol else np.zeros_like(age)

    return w / w.sum(), age, metal, alpha


def prepare(w, age, metal, alpha, alpha_sel):
    ages_u   = np.unique(age)
    metals_u = np.unique(metal)
    alphas_u = np.unique(alpha)

    sfh = np.array([w[age == a].sum() for a in ages_u])

    if alpha_sel is None:
        sel, a_label = np.ones_like(w, dtype=bool), "summed"
    else:
        a_used = alphas_u[np.argmin(np.abs(alphas_u - alpha_sel))]
        sel, a_label = np.isclose(alpha, a_used), f"{a_used:g}"

    Z = np.zeros((len(metals_u), len(ages_u)))
    for a, m, wi in zip(age[sel], metal[sel], w[sel]):
        Z[np.searchsorted(metals_u, m), np.searchsorted(ages_u, a)] += wi

    return ages_u, metals_u, alphas_u, a_label, sfh, Z, 10 ** np.sum(w * np.log10(age))


def edges(x, log=False):
    """Cell edges around the points x (midpoints in log space if log=True)."""
    v = np.log10(x) if log else np.asarray(x, dtype=float)
    if len(v) < 2:
        e = np.array([v[0] - 0.25, v[0] + 0.25])
    else:
        e = np.concatenate([[v[0] - (v[1] - v[0]) / 2],
                            (v[1:] + v[:-1]) / 2,
                            [v[-1] + (v[-1] - v[-2]) / 2]])
    return 10**e if log else e


# --- Load all runs ---
data = {}
for label, base in runs.items():
    w, age, metal, alpha = load_run(base, bin_id)
    data[label] = prepare(w, age, metal, alpha, alpha_sel)
    ages_u, metals_u, alphas_u, a_label, sfh, Z, mean_age = data[label]
    print(f"{label}: ages {ages_u.min():.2f}-{ages_u.max():.2f} Gyr | "
          f"[alpha/Fe] values: {alphas_u} | map slice: {a_label} | mean age {mean_age:.2f} Gyr")

# Shared scales (used only if shared_scales is True)
g_sfh_max = max(d[4].max() for d in data.values()) * 1.05
g_z_max   = max(d[5].max() for d in data.values())
g_met_lo  = min(d[1].min() for d in data.values())
g_met_hi  = max(d[1].max() for d in data.values())
g_x_min   = min(d[0].min() for d in data.values()) / 1.3
g_x_max   = max(d[0].max() for d in data.values()) * 1.3

os.makedirs(outdir, exist_ok=True)

# --- One image per run: SFH on the left, mass fraction map on the right ---
for label, d in data.items():
    ages_u, metals_u, alphas_u, a_label, sfh, Z, mean_age = d

    if shared_scales:
        sfh_max, z_max, met_lo, met_hi = g_sfh_max, g_z_max, g_met_lo, g_met_hi
        x_min, x_max = g_x_min, g_x_max
    else:
        sfh_max, z_max = sfh.max() * 1.05, Z.max()
        met_lo, met_hi = metals_u.min(), metals_u.max()
        x_min, x_max = ages_u.min() / 1.3, ages_u.max() * 1.3

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5.2))

    age_e = edges(ages_u, log=True)

    ax1.bar(age_e[:-1], sfh, width=np.diff(age_e), align="edge", color="C0")
    ax1.set_xscale("log")
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(0, sfh_max)
    ax1.xaxis.set_major_formatter(ScalarFormatter())
    ax1.set_xlabel("Age [Gyr] (log scale)")
    ax1.set_ylabel("#")
    ax1.set_title(f"{label}: Star Formation History; Log-weighted Mean Age: {mean_age:.2f} Gyr")

    im = ax2.pcolormesh(age_e, edges(metals_u), Z, cmap="viridis",
                        shading="flat", vmin=0, vmax=z_max)
    ax2.set_xscale("log")
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(met_lo - 0.1, met_hi + 0.1)
    ax2.xaxis.set_major_formatter(ScalarFormatter())
    ax2.set_xlabel("Age [Gyr] (log scale)")
    ax2.set_ylabel("[M/H]")
    ax2.set_title(f"{label}: Mass Fraction - [alpha/Fe]={a_label}")
    fig.colorbar(im, ax=ax2).set_label("Weight fraction")

    plt.tight_layout(w_pad=4.0)
    outfile = os.path.join(outdir, "sfh_" + re.sub(r"[^A-Za-z0-9]+", "_", label).strip("_") + ".png")
    fig.savefig(outfile, dpi=200, bbox_inches="tight")
    print("Saved", outfile)

plt.show()