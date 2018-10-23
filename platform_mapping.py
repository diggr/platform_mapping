#!/usr/bin/env python3
"""
This file provides the get_platform_mapping function which returns the 
latest version of the platform mapping, which is to be found online
at the projects github page.
If the requests package is missing or the website is not reachable 
a local copy from the dists directory will be fetched.
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

AVAILABLE_DATABASES = ['esrb', 'gamefaqs', 'mediaartdb', 'mobygames', 'ogdb', 'pegi', 'usk']


def get_platform_mapping(database, with_metadata=False, serve_local=no_requests):
    """
    This function gets the platform mapping

    :param database: name of the video game database the mapping should be obtained for
    :param with_metadata: if set, a metadata block will be returned additionally, default: False
    :param serve_local: if set, the local copy will be prefered over the web resource.
    :return: a dict with the mapping, and optionally a dict with the metadata
    """

    if database not in AVAILABLE_DATABASES:
        raise ValueError("{} not in {}".format(database, ", ".join(AVAILABLE_DATABASES)))

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



