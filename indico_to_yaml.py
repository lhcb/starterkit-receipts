#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   indico_to_yaml.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   07.04.2016
# =============================================================================
"""Get indico registration list and convert it to yaml."""

import os
import argparse
import csv
import yaml


def load_csv_registration(file_name):
    """Loads the CSV-formatted registration.

    Assumes the first row contains the column definitions.

    Arguments:
        file_name (str): File to load.

    Returns:
        list: Registrants as `dict` according to the column
            definitions.

    Raises:
        OSError: If the file does not exist.

    """
    if not os.path.exists(file_name):
        raise OSError("Input CSV doesn't exist -> %s" % file_name)
    with open(file_name) as csv_file:
        registrants_csv = [row for row in csv.reader(csv_file, delimiter=',')]
    col_definitions = registrants_csv.pop(0)
    registrants = []
    for registrant_row in registrants_csv:
        registrants.append({col_definitions[index]: val
                            for index, val in enumerate(registrant_row)})
    return registrants


def build_yaml_def(registrants_list):
    """Convert the registrants list into a YAML object.

    Keeps the registrant ID, name, email and university and puts them
    into the 'registrants' YAML list.

    Arguments:
        registrants_list (list): List of dictionaries defining
            the registered people.

    Returns:
        str: YAML string.

    Raises:
        KeyError: If some of the required columns is missing.

    """
    output_list = []
    for registrant in registrants_list:
        output_list.append({'id': registrant['ID'],
                            'name': registrant['Name'],
                            'email': registrant['Email Address'],
                            'institute': registrant['Affiliation'] or '\-'})
    return yaml.dump({'registrants': output_list}, default_flow_style=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', action='store', type=str, help="Input CSV file")
    parser.add_argument('outputfile', action='store', type=str, help="Output YAML file")
    args = parser.parse_args()
    with open(args.outputfile, 'w') as out:
        out.write('---\n')
        out.write(build_yaml_def(load_csv_registration(args.inputfile)))
        out.write('...\n')


# EOF
