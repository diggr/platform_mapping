#!/usr/bin/env python3
"""
Tests the get_platform_mapping function which is provided for the user
"""

import pytest

from .platform_mapping import get_platform_mapping, AVAILABLE_DATABASES


def test_get_platform_mapping():
    """
    Makes a very basic approach to reading the original tab files, and then
    checking its contents against the rendered json files from the API and
    the locally stored versions.
    """
    for database in AVAILABLE_DATABASES:
        with open('tabular_data/{}.tsv'.format(database)) as tab_file:
            # skip header
            tab_file.readline()
            tab_lines = []
            for line in tab_file.readlines():
                tab_lines.append(line.strip().split("\t"))

        for s_local in [True, False]:
            pm = get_platform_mapping(database, with_metadata=False, serve_local=s_local)
            for tab_line, pm_line in zip(tab_lines, pm):
                assert pm[tab_line[0]] == tab_line[1]
