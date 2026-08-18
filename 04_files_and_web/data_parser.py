"""
Core Objective:
Build a light data parser module that demonstrates standard file operations, converting raw CSV records into structured Python data structures, and serializing filtered data out to JSON.

Specification Requirements:
CSV Reader Function: parse_user_csv(file_path: str) -> List[Dict[str, str]]
- Uses csv.DictReader to safely read tabular data from a CSV file.
- Handles FileNotFoundError gracefully with a clean log statement.
- Returns a list of dictionaries representing the dataset rows.
Data Transformer & Serializer: export_to_json(data: List[Dict[str, Any]], output_path: str) -> None
- Filters or formats the dataset (e.g., extracting active user records).
- Writes the processed data to a target JSON file using json.dump() with indent=4 formatting.
Context Manager File Handler: append_system_log(log_path: str, message: str) -> None
- Demonstrates Colt's standard file append mode ("a") using with open(...) context managers to append ISO/system log entries safely.
"""

import csv
from typing import List, Dict


def parse_user_csv(file_path: str) -> List[Dict[str, str]]:
    try:
        with open(file_path) as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        print("The file you are looking for does not exist")
        return []


if __name__ == "__main__":
    print(parse_user_csv("04_files_and_web/ecommerce_sales.csv"))
    print("\n")
    print(parse_user_csv("cat.csv"))
