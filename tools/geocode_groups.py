"""One-off: find a map point for each town in tools/network_groups.csv and save it to tools/network_geo.json.
Uses OpenStreetMap Nominatim (town names only, one request a second). Groups with no town get the middle of their council area.
Run again only when the group list changes; the build reads the saved file and makes no network calls."""
import csv, json, os, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BOX = (-30.9, -27.9, 151.5, 153.7)  # south, north, west, east: the Northern Rivers region
UA = "nrcra-review-site/1.0 (kwanvero@gmail.com)"


def ask(q):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({"q": q, "format": "json", "limit": 1, "countrycodes": "au"})
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20) as r:
        data = json.load(r)
    time.sleep(1.1)
    if not data:
        return None
    lat, lon = float(data[0]["lat"]), float(data[0]["lon"])
    return (lat, lon) if BOX[0] <= lat <= BOX[1] and BOX[2] <= lon <= BOX[3] else None


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "network_groups.csv"), newline="", encoding="utf-8")))
    out = {}
    for loc, lga in sorted({(r["Location"], r["LGA"]) for r in rows}):
        key = f"{loc}|{lga}"
        got, kind = (None, "town")
        if loc:
            got = ask(f"{loc}, {lga}, NSW, Australia") or ask(f"{loc}, NSW, Australia")
        if not got:
            got, kind = ask(f"{lga}, NSW, Australia"), "lga"
        print(key, got, kind)
        if got:
            out[key] = [round(got[0], 5), round(got[1], 5), kind]
    json.dump(out, open(os.path.join(HERE, "network_geo.json"), "w"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
