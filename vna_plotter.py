#!/usr/bin/env python3

"""
VNA Plotter Script
Plots VNA measurement data from CSV files.
"""

import sys
import os
import csv


def main():
    if len(sys.argv) < 2:
        print("Usage: python vna_plotter.py <input_file.csv> [plot_title]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Extract file name without extension for default plot title
    file_name_without_ext = os.path.splitext(os.path.basename(input_file))[0]
    
    # Use file name as default plot title, or override with command line argument
    plot_title = sys.argv[2] if len(sys.argv) > 2 else file_name_without_ext
    
    try:
        # Read and process the CSV file
        with open(input_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            data = list(reader)
        
        print(f"Processing file: {input_file}")
        print(f"Plot title: {plot_title}")
        print(f"Data columns: {header}")
        print(f"Number of data rows: {len(data)}")
        
        # For demonstration purposes, just print the configuration
        # In a real implementation, this would create the actual plot
        print("\n--- VNA Plot Configuration ---")
        print(f"Title: {plot_title}")
        print(f"Input file: {input_file}")
        print(f"Columns: {', '.join(header) if header else 'No header'}")
        
        # This is where the actual plotting would happen with matplotlib
        # For now, we just demonstrate the title logic works correctly
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()