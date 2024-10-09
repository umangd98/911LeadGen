import os
import csv
import json
import re

import os
import csv
import json
import re

# Function to extract and attempt to fix JSON objects and arrays from text
def extract_and_fix_json_from_text(text):
    # Replace single quotes with double quotes
    text = text.replace("'", '"')

    # Regex pattern to find JSON objects or arrays
    json_pattern = re.compile(r'(\{.*?\}|\[.*?\])', re.DOTALL)
    matches = json_pattern.findall(text)

    # Attempt to fix common JSON issues
    fixed_matches = []
    for match in matches:
        # Remove trailing commas before closing braces or brackets
        match = re.sub(r',\s*([\]}])', r'\1', match)
        # Ensure keys are properly quoted
        match = re.sub(r'(\w+):', r'"\1":', match)
        fixed_matches.append(match)
    
    return fixed_matches

# Function to process the input file and create the CSV
def process_file(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract and fix all JSON objects and arrays from the content
    json_strings = extract_and_fix_json_from_text(content)

    # Prepare the CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['address', 'context'])
        writer.writeheader()

        for json_str in json_strings:
            try:
                # Parse the JSON object or array
                json_data = json.loads(json_str)
                
                # Handle if the extracted JSON is an array of objects
                if isinstance(json_data, list):
                    for entry in json_data:
                        if isinstance(entry, dict) and 'address' in entry and 'context' in entry:
                            writer.writerow({'address': entry['address'], 'context': entry['context']})
                elif isinstance(json_data, dict) and 'address' in json_data and 'context' in json_data:
                    writer.writerow({'address': json_data['address'], 'context': json_data['context']})
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {e}")
                continue  # Skip to the next JSON string

    print(f"Data successfully written to {output_csv}.")

# Example usage
input_file = './Dallas County/Sachse Police and Fire Aug 13/Sachse Police and Fire Aug 13.txt'
output_csv = './Dallas County/Sachse Police and Fire Aug 13/Sachse Police and Fire Aug 13.csv'

process_file(input_file, output_csv)
