import os
import yaml
import pathlib

CONF_TEMPLATE = """
shiftsubs:
    adsense:
"""


def get_options():
    home_path = pathlib.Path.home()
    path = f"{home_path}/shiftsubs.conf.yml"

    if not os.path.exists(path):
        with open(path, "w+") as f:
            f.write(CONF_TEMPLATE)

    config = None
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)

    if config is not None:
        return config
    else:
        raise Exception("cannot initialise configuration file for netscope")


CUSTOM_PROTOCOLS_RULES_TEMPLATE = """
custom_rules: []
"""


def write_options(options):
    new_options_str = yaml.dump(options)
    home_path = pathlib.Path.home()
    path = f"{home_path}/shiftsubs.conf.yml"

    with open(path, "w+") as f:
        f.write(new_options_str)
