"""Clean the Alliance group list from Groups.xlsx (visible rows of the Location sheet only) into the CSV the site and Wix use.

Usage: python3 tools/clean_groups.py /path/to/Groups.xlsx
Needs openpyxl. Writes tools/network_groups.csv (Wix import: ID, Group Name, Location, LGA, Aboriginal Country, Website, Facebook).
"""
import csv
import re
import sys

import openpyxl

OUT = "tools/network_groups.csv"

# The "Comms assets" tab has its group names out of step with its links, so links are matched to groups by what the URL says
# (comms row -> group). Row 10 keeps only the website (its Facebook id belongs to Bangalow), row 26 keeps only Facebook
# (its website is a NSW memorials register) and row 59 keeps only the website. Ambiguous rows (13, 34, 56) are left out.
COMMS = {
    3: "Main Arm Disaster Recovery Inc", 4: "Bangalow Resilience Network", 5: "Coorabell CRT",
    6: "Hinterland CRT / Federal, Eureka and Goonengerry Community Resilience Team", 7: "Mullumbimby & District Neighbourhood Centre",
    10: "Blicks Community Inc", 11: "Gurehlgam Grafton", 12: "ICOPE (Iluka Community Organisation Planning for Emergencies)",
    14: "The New School of Arts Neighbourhood House", 15: "Woombah Residents Association (Woombah&Mororo)",
    16: "Creative Communities Connect / Wadeville Emergency Response Team", 17: "Kyogle Together Inc", 18: "Tabulum Hub",
    19: "Minyon Resilience Network", 20: "Repentance Creek Public Hall Inc", 22: "Nimbin Disaster Resilience Group",
    23: "Nimbin Neighbourhood & Information Centre", 24: "Rock Valley CRT", 25: "The Channon Resilience Inc",
    26: "Whian Whian Emergency Hub", 27: "Resilient Lismore Inc", 28: "Clunes Old School Assoc.",
    29: "Wardell CORE (Wardell Community Organised Resilience Effort)", 30: "Mid Richmond Neighbourhood Centre (Evans Head)",
    33: "Burringbar Resilience Network CRT", 35: "Chinderah and Surrounds Peoples Hub", 36: "Fingal Head CRT", 37: "Resilient Uki",
    38: "Murwillumbah Community Centre", 40: "Together Pottsville Inc", 41: "Tumbulgum Community Association",
    42: "Resilience Tyalgum", 45: "Resilient Suffolk", 53: "Clunes Coronation Hall", 57: "Mudyala Aboriginal Corporation",
    59: "Burringbar Community Association", 63: "Pottsville Beach Neighbourhood Centre",
}
DROP_FB = {10, 59}
DROP_WEB = {26}
EXTRA_WEB = {"Nimbin Disaster Resilience Group": "https://nnic.org.au/pub/index.php/disasters"}


def url(t):
    t = tidy(t if t not in (None, "None") else "")
    if not t or "@" in t:
        return ""
    return t if t.startswith("http") else "https://" + t
EXCLUDE = ("not a member yet",)


def tidy(t):
    return re.sub(r"\s+", " ", (t or "").strip())


def main(path):
    wb = openpyxl.load_workbook(path)
    ws = wb["Location"]
    cs = wb["Comms assets"]
    links = {}
    for row, grp in COMMS.items():
        web = "" if row in DROP_WEB else url(cs.cell(row, 4).value)
        fb = "" if row in DROP_FB else url(cs.cell(row, 5).value)
        links[grp] = [EXTRA_WEB.get(grp, web), fb]
    hidden = {k for k, v in ws.row_dimensions.items() if v.hidden}
    seen = {}
    skipped = []
    for i, r in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        name, loc, lga = tidy(r[0]), tidy(r[2]), tidy(r[3])
        if i in hidden or not name:
            continue
        if any(x in name.lower() for x in EXCLUDE):
            skipped.append(name)
            continue
        lga_name, _, country = (p.strip() for p in lga.partition("—"))
        key = re.sub(r"[^a-z0-9]", "", name.split("(")[0].lower())
        if key in seen:
            if not seen[key][1] and loc:
                seen[key][1] = loc
            if len(name) > len(seen[key][0]):
                seen[key][0] = name
            continue
        seen[key] = [name, loc, lga_name, country]
    rows = sorted(seen.values(), key=lambda r: (r[2].lower(), r[0].lower()))
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Group Name", "Location", "LGA", "Aboriginal Country", "Website", "Facebook"])
        for n, r in enumerate(rows, 1):
            w.writerow([f"grp-{n:03d}"] + r + links.get(r[0], ["", ""]))
    print(len(rows), "groups written; excluded:", skipped)


main(sys.argv[1])
