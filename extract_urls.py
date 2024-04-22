#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ijson
import argparse


def extract_matching_locations(file_path):
    """Returns a list of URLs from the nested 'location' field for matches of 'PPO' and 'New York' in the description within that nested location."""
    urls = []

    with open(file_path, 'rb') as file:
        items = ijson.items(file, 'reporting_structure.item')
        for item in items:
            if 'in_network_files' in item and isinstance(item['in_network_files'], list):
                for nested_dict in item['in_network_files']:
                    if 'description' in nested_dict and 'location' in nested_dict:
                        description = nested_dict['description']
                        if 'PPO' in description and 'New York' in description:
                            urls.append(nested_dict['location'])
    return urls


def main(input_file, output_file):
    matching_urls = extract_matching_locations(input_file)
    with open(output_file, 'w') as f:
        for url in matching_urls:
            f.write(url + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract URLs for Anthem's PPO in New York from a large JSON file.")
    parser.add_argument('input_file', type=str,
                        help='Path to the input JSON file.')
    parser.add_argument('output_file', type=str,
                        help='Path to the output text file where URLs will be saved.')

    args = parser.parse_args()

    main(args.input_file, args.output_file)
