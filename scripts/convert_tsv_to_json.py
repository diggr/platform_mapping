#!/usr/bin/env python3
"""
Converts platform mapping tsv and csv files to json files.
"""
import csv
import datetime
import json

from os.path import join


# CONFIGURATION

## DELIMITER OF THE BASE DATA
DELIMITER="\t"

## BASE PATH IS PREPENDED TO ALL OTHER DATA PATHS 
BASE_PATH = ".."

## SKELETON IS LOCATED AT
SKELETON_FILENAME = join( BASE_PATH, "skeleton.json")

## MAPPING DATA IS LOCATED AT
MAPPING_PATH = join(BASE_PATH, "tabular_data")
MAPPING_FILENAMES = { "ESRB" : "esrb.tsv",
                      "GameFAQs": "gamefaqs.tsv",
                      "MediaArtDB": "mediaart.tsv",
                      "Mobygames": "mobygames.tsv",
                      "OGDB": "ogdb.tsv",
                      "PEGI": "pegi.tsv",
                      "USK": "usk.tsv" }
MAPPING_FILES = { m_title:join(MAPPING_PATH, m_filename) for m_title, m_filename in MAPPING_FILENAMES.items() }

## OUTPUT 
OUT_PATH = join(BASE_PATH, "json_data")
OUT_EXT = ".json"

# FUNCTIONS
def tsv_to_json(mapping_file, delimiter=DELIMITER):
    """
    Opens a tabular (default) or any other kind of two-column csv-data
    and returns its content as python object
    """
    output = dict()
    with open(mapping_file) as mfile:
        reader = csv.reader(mfile, delimiter=delimiter)
        for row in reader:
            output[row[0]] = row[1]
    return output


def load_skeleton(skeleton_filename=SKELETON_FILENAME):
    """
    Loads a json file and returns its content as
    python object.
    """
    with open(skeleton_filename) as sfile:
        return json.load(sfile)


def create_static_rest_files(mapping_files=MAPPING_FILES, 
                             delimiter=DELIMITER,
                             out_path=OUT_PATH,
                             out_ext=OUT_EXT,
                             skeleton_filename=SKELETON_FILENAME):
    """
    Actual conversion function. Takes a list of mapping files and
    writes the json output files.
    """
    # Gather
    skeleton = load_skeleton(skeleton_filename)
    for m_title, m_filename in mapping_files.items():
        print("Converting {} ...".format(m_filename))
        mapping = tsv_to_json(m_filename)
        
        # Combine
        out_data = skeleton.copy()
        out_data["name"] = m_title
        out_data["date"] = datetime.datetime.now().replace(microsecond=0).isoformat()
        out_data["mapping"] = mapping

        # Save
        out_file = join(out_path, m_title.lower()+out_ext)
        with open(out_file, "w") as outfile:
            json.dump(out_data, outfile, indent=4)


if __name__ == "__main__":
    create_static_rest_files()
