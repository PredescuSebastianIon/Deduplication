# Database Deduplication

This project implements a deduplication for some company data.<br>
The main goal was to identify what datas are doubled in the records using fuzzy matching techniques.

## Overview

This project demonstrates:
- Data Normalization:
    Standardizes company names and countries by removing noise such as suffixes and non-alphanumeric characters.
- Fuzzy Deduplication:
    Uses fuzzy matching (via RapidFuzz) to compare records that are similar but not identical.

## Instalation
1. Clone Repository

    ```bash
    git clone https://github.com/YourUser/YourRepo.git
    cd deduplication_database
2. Install Dependencies

    ```bash
    pip install -r requirements.txt


## Usage

- Run the deduplication pipeline:

        ```bash
        python main.py