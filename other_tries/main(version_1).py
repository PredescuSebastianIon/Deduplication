import pandas as pd
from rapidfuzz import fuzz
import re

def normalize(string):
    if pd.isna(string):
        return ''
    string = string.lower()
    # Removing these types of suffix
    # For exemple Google Inc vs Google Llc
    string = re.sub(r'\b(inc|ltd|llc|corp|co|s\.a|srl|gmbh)\b', '', string)
    # Removing any type of non alfanumerics characters
    string = re.sub(r'\W+', '', string)
    # Removing any type of whitespaces from the word
    string = re.sub(r'\s+', '', string)
    return string.strip()

def similarity_function(file):
    file = file.reset_index(drop = True)
    groups = {}
    group_id = 0
    marked = set()

    for i in range(len(file)):
        if i in marked:
            continue
        name_i = file.loc[i, 'normalized_name']
        domain_i = file.loc[i, 'website_domain']
        country_i = file.loc[i, 'main_country']

        # Starting a new group
        members = [i]
        for j in range(i + 1, len(file)):
            if j in marked:
                continue
            name_j = file.loc[j, 'normalized_name']
            domain_j = file.loc[j, 'website_domain']
            country_j = file.loc[j, 'main_country']

            score_name = fuzz.token_sort_ratio(name_i, name_j)
            score_domain = fuzz.token_sort_ratio(domain_i, domain_j)
            score_country = fuzz.token_sort_ratio(country_i, country_j)

            score_overall = (score_name + score_domain + score_country) / 3
            if score_overall > 90.00:
                members.append(j)
                marked.add(j)

        for m in members:
            groups[m] = group_id
        
        group_id += 1
    file['group_id'] = file.index.map(groups)
    return file


file = pd.read_parquet('veridion_entity_resolution_challenge.snappy.parquet', engine='pyarrow')
print("Original:", file.shape)
file['normalized_name'] = file['company_name'].apply(normalize)

# Deduplicate using normalized name, country, domain
new_file = file.drop_duplicates(subset=['normalized_name', 'main_country', 'website_domain'])


# new_file = similarity_function(new_file)



print("Deduplicated:", new_file.shape)
