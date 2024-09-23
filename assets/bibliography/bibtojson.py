import bibtexparser
import json
import argparse 
import os

parser = argparse.ArgumentParser()

parser.add_argument('-f', type=str, help="bibtex file path")

args = parser.parse_args()

with open(args.f, 'r') as bib_file:
    bib_database = bibtexparser.load(bib_file) 

json_file_name = os.path.basename(args.f).split(".")[0] + ".json"

with open(os.path.join("_data/", json_file_name), "w") as json_file: 
    bib_as_json = json.dump(bib_database.entries, json_file, indent=4) 
