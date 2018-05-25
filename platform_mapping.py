#!/usr/bin/env python3
"""
This file provides a class which

"""

import json

no_requests = False
try:
    import requests
except ImportError:
    no_requests = True
    print("requests package not found. Falling back to local platform mapping")

from os.path import join, dirname, abspath

BASE_PATH = dirname(abspath(__file__))
DATA_PATH = join(BASE_PATH, "dist")
BASE_URL = "https://diggr.github.io/platform_mapping/{}.json"

AVAILABLE_PLATFORMS = ['esrb', 'gamefaqs', 'mediaartdb', 'mobygames', 'ogdb', 'pegi', 'usk']


def get_platform_mapping(database, with_metadata=False):
    """
    This function gets the platform mapping

    :param database: name of the video game database the mapping should be obtained for
    :param with_metadata: if set, a metadata block will be returned additionally, default: False
    :return: a dict with the mapping, and optionally a dict with the metadata
    """

    if database not in AVAILABLE_PLATFORMS:
        raise ValueError("{} not in {}".format(database, ", ".join(AVAILABLE_PLATFORMS)))

    fetch_successful = False

    if not no_requests:
        response = requests.get(BASE_URL.format(database))
        if response.status_code == 200:
            mapping = json.loads(response.text)
            fetch_successful = True

    if not fetch_successful:
        with open(join(DATA_PATH, "{}.json".format(database))) as mapping_file:
            mapping = json.load(mapping_file)

    if with_metadata:
        return mapping['mapping'], mapping['meta']
    else:
        return mapping['mapping']



