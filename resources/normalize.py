import pandas as pd
import re


def just_lower_case(string):
    if pd.isna(string):
        return pd.NA
    string = string.lower()
    return string

def normalize(string):
    if pd.isna(string):
        return pd.NA
    string = string.lower()
    # Removing these types of suffix
    # For exemple Google Inc vs Google Llc
    string = re.sub(r'\b(inc|ltd|llc|corp|co|s\.a|srl|gmbh)\b', '', string)
    # Removing any type of non alfanumerics characters
    string = re.sub(r'\W+', '', string)
    # Removing any type of whitespaces from the word
    string = re.sub(r'\s+', '', string)
    return string.strip()