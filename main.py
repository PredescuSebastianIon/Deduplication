import pandas as pd
import re, time, sys
from resources.normalize import normalize, just_lower_case
from resources.similarity import similarity_function
from resources.most_complited_columns import percentage


# Start the program
start_time = time.time()
# Read the file
file = pd.read_parquet('data/veridion_entity_resolution_challenge.snappy.parquet', engine='pyarrow')

# Let's normalized the company_name and main_country
file['normalized_name'] = file['company_name'].apply(normalize)
file['normalized_country'] = file['main_country'].apply(normalize)
file['normalized_country_code'] = file['main_country_code'].apply(normalize)
file['normalized_region'] = file['main_region'].apply(normalize)
file['normalized_website'] = file['website_domain'].apply(normalize)
file['normalized_locations'] = file['locations'].apply(normalize)

# Let's find out what are the most relevant columns from this database
percentage(file)

print("Original rows:", file.shape[0])
# Apply fuzzy deduplication
file = similarity_function(file)
print("After deduplication deduplication:", file.shape[0])
# Execution time
end_time = time.time()
print(f"------ {end_time - start_time} seconds -------")

# Save the final file as a physical file
# file.to_parquet('veridion_deduplicated(5).parquet', index=False)