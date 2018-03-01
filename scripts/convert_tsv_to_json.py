#!/usr/bin/env python3
"""
Converts platform mapping tsv and csv files to json files.
"""
import csv
import datetime
import json

from os.path import join, abspath, dirname


# CONFIGURATION

## DELIMITER OF THE BASE DATA
DELIMITER="\t"

## BASE PATH IS PREPENDED TO ALL OTHER DATA PATHS 
BASE_PATH = join(dirname(abspath(__file__)), "..")

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
                      "USK": "usk.tsv",
                      "Diggr Vocabulary": "diggr_vocab.tsv"}
MAPPING_FILES = { m_title:join(MAPPING_PATH, m_filename) for m_title, m_filename in MAPPING_FILENAMES.items() }

## PLATFORM GROUP FILE
PLATFORM_GROUP_FILE = join(MAPPING_PATH, "platform_groups.tsv")

## OUTPUT 
OUT_PATH = join(BASE_PATH, "json_data")
OUT_EXT = ".json"
PLATFORM_GROUP_OUTFILE = join(OUT_PATH, "platform_groups"+OUT_EXT)

# FUNCTIONS
def mapping_to_json(mapping_file, delimiter=DELIMITER):
    """
    Opens a tabular (default) or any other kind of two-column csv-data
    and returns its content as python object
    """
    output = dict()
    with open(mapping_file) as mfile:
        reader = csv.reader(mfile, delimiter=delimiter)
        
        # skip header
        next(reader)
        
        for row in reader:
            output[row[0]] = row[1]
    return output

def platform_group_to_json(platform_group_file, delimiter=DELIMITER):
    with open(platform_group_file) as pffile:
        reader = csv.reader(pffile, delimiter=delimiter)
        
        result = {}
        groupname = ""
        group = list()

        for row in reader:
            platform_name = row[1].strip()
            try:
                result[row[0]].append(platform_name)
            except KeyError:
                result[row[0]] = [platform_name]
           
        return result 

def load_skeleton(skeleton_filename=SKELETON_FILENAME):
    """
    Loads a json file and returns its content as
    python object.
    """
    with open(skeleton_filename) as sfile:
        return json.load(sfile)


def create_static_rest_files(mapping_files=MAPPING_FILES, 
                             platform_group_file=PLATFORM_GROUP_FILE,
                             platform_group_outfile=PLATFORM_GROUP_OUTFILE,
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
    skeleton["date"] = datetime.datetime.now().replace(microsecond=0).isoformat()

    for m_title, m_filename in mapping_files.items():
        print("Converting {} ...".format(m_title))
        mapping = mapping_to_json(m_filename)
        
        # Combine
        out_data = skeleton.copy()
        out_data["name"] = m_title
        out_data["mapping"] = mapping

        # Save
        out_file = join(out_path, m_title.lower().replace(" ", "_")+out_ext)
        with open(out_file, "w") as outfile:
            json.dump(out_data, outfile, indent=4)

    #Platform Group
    print("Converting Platform Groups ...")
    platform_groups = platform_group_to_json(platform_group_file)
    pf_result = skeleton.copy()
    pf_result["name"] = "Platform Groups"
    pf_result["platform_groups"] = platform_groups
    with open(platform_group_outfile, "w") as outfile:
        json.dump(pf_result, outfile, indent=4)

if __name__ == "__main__":
    create_static_rest_files()
