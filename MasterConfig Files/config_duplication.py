import yaml, copy, os

base = yaml.safe_load(open("MasterConfig_13_ESO120-016_singlebin.yaml"))

galaxy = "ESO120-016"                                  # galaxy name
folder = "13_ESO120-016"                               # parent results folder
setup  = "iDR1_SN50_2.5_LW_4750-8900_singlebin"        # the rest of your run name

config_dir = os.path.join( galaxy)       # where the new configs go
os.makedirs(config_dir, exist_ok=True)

models = {
    "MILES":   dict(LSF_TEMP="lsf_MILES",
                    TEMPLATE_SET="miles",   LIBRARY="MILES/"),
    "alphaMC": dict(LSF_TEMP="lsf_alphaMC_highres.txt",
                    TEMPLATE_SET="alphaMC", LIBRARY="alphaMC/"),
    "XSL":     dict(LSF_TEMP="lsf_xsl_ssp.txt",
                    TEMPLATE_SET="xsl_ssp", LIBRARY="xsl_ssp/"),
}

for name, sfh in models.items():
    cfg = copy.deepcopy(base)
    run_id = f"{galaxy}_{setup}_{name}"
    cfg["GENERAL"]["RUN_ID"] = run_id
    cfg["GENERAL"]["OUTPUT"] = folder
    cfg["SFH"].update(sfh)
    path = os.path.join(config_dir, f"config_{galaxy}_{name}.yaml")
    with open(path, "w") as f:
        yaml.safe_dump(cfg, f, sort_keys=False)
    print("Wrote", path)