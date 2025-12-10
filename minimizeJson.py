#!/usr/bin/env python3
"""
JSON Minimizer - Loads a JSON file and resaves it with minimal whitespace.
Usage: python3 minimizeJson.py <input_file>
"""

import json
import sys
import os

def minimize_json(input_file):
    """
    Load a JSON file and resave it with minimal whitespace.
    
    Args:
        input_file (str): Path to the input JSON file
    """
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    try:
        # Load the JSON file
        print(f"Loading JSON from: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Get original file size
        original_size = os.path.getsize(input_file)
        
        # Save with minimal whitespace (no indentation, no extra spaces)
        print(f"Minimizing and saving to: {input_file}")
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'), ensure_ascii=False)
        
        # Get new file size
        new_size = os.path.getsize(input_file)
        
        # Report size reduction
        size_reduction = original_size - new_size
        percentage_reduction = (size_reduction / original_size) * 100 if original_size > 0 else 0
        
        print(f"Original size: {original_size:,} bytes")
        print(f"Minimized size: {new_size:,} bytes")
        print(f"Size reduction: {size_reduction:,} bytes ({percentage_reduction:.1f}%)")
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{input_file}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file '{input_file}': {e}")
        sys.exit(1)

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python3 minimizeJson.py <input_file>")
        print("Example: python3 minimizeJson.py jwb_min.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    minimize_json(input_file)
    print("JSON minimization complete!")

if __name__ == "__main__":
    main()
