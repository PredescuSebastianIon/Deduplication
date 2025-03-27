# Database Deduplication

This project implements a deduplication for some company data.<br>
The main goal was to identify what datas are doubled in the records using fuzzy matching techniques.

## Overview

This project demonstrates:
- Data Normalization:
    Standardizes company names and countries by removing noise such as suffixes and non-alphanumeric characters.
- Fuzzy Deduplication:
    Uses fuzzy matching (via RapidFuzz) to compare records that are similar but not identical.

## Installation
1. Clone Repository

    ```bash
    git clone https://github.com/YourUser/YourRepo.git
    cd deduplication_database
2. Install Dependencies

    ```bash
    pip install -r requirements.txt

## Usage

- Run the deduplication pipeline:

        python main.py

## How it works

- Normalization:<br>
    The normalize function in resources/normalize.py converts company names to lowercase, removes common suffixes (like "Inc" or "LLC"), and strips non-alphanumeric characters.

- Fuzzy matching:<br>
    The similarity_function in resources/similarity.py uses the RapidFuzz library to calculate similarity scores between records. Records with a similarity score above the threshold are grouped together.

- Grouping and Deduplication:<br>
    After fuzzy matching, the script assigns a group ID to each cluster of similar records and retains one representative record from each group.
