from rapidfuzz import fuzz
import pandas as pd


def compare_2_rows(block, i, j, relevant_columns):
    cnt = 0
    score = 0
    for coloana in relevant_columns:
        val_i = block.loc[i, coloana]
        val_j = block.loc[j, coloana]
        if pd.isnull(val_i) or pd.isnull(val_j):
            continue
        # If values are not null
        cnt += 1
        similiraty = fuzz.token_sort_ratio(str(val_i), str(val_j))
        score += similiraty
                
        if cnt > 0:
            score = score / cnt
        else:
            score = 0
    return score

def similarity_function(file):
    relevant_columns = ['normalized_name', 'normalized_region', 'normalized_country_code']
    file = file.reset_index(drop = True)
    groups = {}
    group_id = 0
    file['index'] = file.index  # Preserve original index

    # I am taking to compare only the companies that are in the same country
    # Also their normalize name should start with the same letter to have sense to compare them
    for tuple_key, block in file.groupby(['normalized_country', 'normalized_website']):
        block = block.reset_index()
        local_marked = set()

        for i in range(len(block)):
            if i in local_marked:
                continue

            members = [i]
            for j in range(i + 1, len(block)):
                # check if already is assigned in a group
                if j in local_marked:
                    continue

                score = compare_2_rows(block, i, j, relevant_columns)
                if score > 90:
                    members.append(j)
                    local_marked.add(j)

            # assign the group_id for every member
            for m in members:
                original_index = block.loc[m, 'index']
                groups[original_index] = group_id

            group_id += 1

    file['group_id'] = file['index'].map(groups)
    file.drop(columns = ['index'], inplace = True)
    file = file.drop_duplicates(subset=['group_id'])
    return file