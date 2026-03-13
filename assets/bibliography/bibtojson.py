import bibtexparser
import json
import argparse 
import os


file_path = "assets/bibliography/publications.bib"

with open(file_path, 'r') as bib_file:
    bib_database = bibtexparser.load(bib_file) 

for entry in bib_database.entries:
    authors_list = entry["author"].split(" and ")
    for i, author in enumerate(authors_list):
        authors_list[i] = " ".join(author.split(",")[::-1])
        if i == len(authors_list)-1:
            authors_list[i] = "and " + authors_list[i]
    
    authors = ", ".join(authors_list)
    entry["author"] = authors

json_file_name = os.path.basename(file_path).split(".")[0] + ".json"

with open(os.path.join("_data/", json_file_name), "w") as json_file: 
    bib_as_json = json.dump(bib_database.entries, json_file, indent=4) 
