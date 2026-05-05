from pathlib import Path


ALIASES = {
    "United States of America": "United States",
    "United States": "United States",
    "Czechia": "Czech Republic",
    "Dem. Rep. Congo": "Democratic Republic of the Congo",
    "Republic of Congo": "Republic of the Congo",
    "Dominican Rep.": "Dominican Republic",
    "Central African Rep.": "Central African Republic",
    "Eq. Guinea": "Equatorial Guinea",
    "eSwatini": "Eswatini",
    "S. Sudan": "South Sudan",
    "Bosnia and Herz.": "Bosnia and Herzegovina",
    "Solomon Is.": "Solomon Islands",
}


def _norm_name(name):
    return " ".join(str(name).strip().casefold().split())


def _flag_path(entry):
    for key in ("flag_4x3", "flag", "path", "file"):
        if key in entry:
            return entry[key]
    iso2 = entry.get("iso2") or entry.get("code") or entry.get("alpha2")
    if iso2:
        return str(Path("flags") / "4x3" / f"{str(iso2).lower()}.svg")
    return None


def build_country_lookup(countries_geojson, flag_index):
    """Return ``{iso3: {...}}`` by joining country features to flag metadata.

    The country polygons use ISO-3 codes while the flag files use ISO-2 codes.
    This helper joins them by country name and keeps unmatched countries usable
    with ``flag_path=None``.
    """
    if isinstance(flag_index, dict):
        raw_entries = flag_index.values()
    else:
        raw_entries = flag_index

    by_name = {}
    for entry in raw_entries:
        name = entry.get("name") or entry.get("country") or entry.get("Name")
        if not name:
            continue
        iso2 = entry.get("iso2") or entry.get("code") or entry.get("alpha2")
        by_name[_norm_name(name)] = {
            "name": name,
            "iso2": str(iso2).lower() if iso2 else None,
            "flag_path": _flag_path(entry),
        }

    lookup = {}
    for feature in countries_geojson.get("features", []):
        props = feature.get("properties", {})
        name = props.get("ADMIN") or props.get("name") or props.get("NAME")
        iso3 = (
            props.get("ISO_A3")
            or props.get("ISO3166-1-Alpha-3")
            or props.get("iso3")
            or props.get("adm0_a3")
        )
        if not iso3 or not name:
            continue
        match_name = ALIASES.get(name, name)
        flag_meta = by_name.get(_norm_name(match_name), {})
        lookup[iso3] = {
            "name": name,
            "iso2": flag_meta.get("iso2"),
            "flag_path": flag_meta.get("flag_path"),
            "feature": feature,
        }

    return lookup
