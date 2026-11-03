"""Writes a CSV that Google My Maps can import (Import, choose Latitude and Longitude columns, title column Name).
Same points as the prototype map. Usage: python3 tools/export_mymaps_csv.py <out.csv>"""
import csv, sys
import build_teal as T

with open(sys.argv[1], "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Description", "Website or Facebook", "Latitude", "Longitude"])
    for g in T.map_points():
        w.writerow([g["n"], g["p"], g["u"], g["lat"], g["lon"]])
