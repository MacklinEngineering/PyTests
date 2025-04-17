#Partner Names: Nyah Macklin and Tau Adegun
#Collaboration: Tau wrote code to read the CSV, Nyah wrote code to write the CSV. 
#Reads a CSV file 'country_full.csv' and splits the countries into separate CSV files based on region.

import csv

# Define the input CSV file name
INPUT_FILE = 'country_full.csv'

def split_country_file(input_file):
    """Reads country_full.csv input file and places the countries based on regions into separate files with name and region columns.
    """
    try:
        # Open the input CSV file for reading
        with open(input_file, mode='r', encoding='utf-8') as file:
            #Use CSV DictReader to read files
            #place that info in a dictionary
            reader = csv.DictReader(file)
            regions = {}

            # Read each row in the CSV file
            for row in reader:
                region = row['region']
                if region not in regions:
                    regions[region] = []
                regions[region].append(row)

            # Iterate over each region
            # write the specified countries to separate files
            for region, rows in regions.items():
                if not region:  # Skip empty regions
                    continue
                #Replace spaces with underscores for proper python filenames
                filename = f"{region.strip().replace(' ', '_')}.csv"
                try:
                    # Open the output CSV file to write
                    with open(filename, mode='w', newline='', encoding='utf-8') as outfile:
                        # Define the fields for the output file
                        fields = ['name', 'region']
                        writer = csv.DictWriter(outfile, fieldnames=fields)
                        writer.writeheader()
                        # Write each country's name and region to output file
                        for row in rows:
                            writer.writerow({'name': row['name'], 'region': row['region']})
                    print(f"Created file: {filename}")
                #Handle Errors    
                except (IOError, PermissionError) as e:
                    print(f"Error writing file {filename}: {e}")

    #Additional Error Handling
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except IOError as e:
        print(f"Read Error {input_file}: {e}")

# Run the function
split_country_file(INPUT_FILE)
