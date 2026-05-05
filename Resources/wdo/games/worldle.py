import random

from wdo.geometry.bbox import bbox_from_feature
from wdo.geometry.bearing import bearing_to_compass, initial_bearing
from wdo.geometry.distance import haversine_km, haversine_miles


ARROWS = {
    "N": "↑",
    "NE": "↗",
    "E": "→",
    "SE": "↘",
    "S": "↓",
    "SW": "↙",
    "W": "←",
    "NW": "↖",
}


def _feature_name(feature):
    props = feature.get("properties", {})
    return props.get("ADMIN") or props.get("name") or props.get("NAME") or "Unknown"


def _feature_iso3(feature):
    props = feature.get("properties", {})
    return (
        props.get("ISO_A3")
        or props.get("ISO3166-1-Alpha-3")
        or props.get("iso3")
        or props.get("adm0_a3")
    )


def _iter_lon_lat(coords):
    if not coords:
        return
    first = coords[0]
    if isinstance(first, (int, float)) and len(coords) >= 2:
        yield (coords[0], coords[1])
        return
    for item in coords:
        yield from _iter_lon_lat(item)


def choose_target(features, seed=None):
    """Choose a target feature for Worldle++."""
    features = list(features)
    if not features:
        raise ValueError("features must contain at least one feature")
    return random.Random(seed).choice(features)


def feature_center(feature, method="bbox"):
    """Return representative center point of a feature."""
    if method == "bbox":
        min_lon, min_lat, max_lon, max_lat = bbox_from_feature(feature)
        return ((min_lat + max_lat) / 2, (min_lon + max_lon) / 2)

    if method == "mean":
        coords = list(_iter_lon_lat(feature.get("geometry", {}).get("coordinates", [])))
        if not coords:
            raise ValueError("Feature has no coordinates")
        lon = sum(point[0] for point in coords) / len(coords)
        lat = sum(point[1] for point in coords) / len(coords)
        return (lat, lon)

    raise ValueError("method must be 'bbox' or 'mean'")


def guess_feedback(guess_feature, target_feature):
    """Return distance, bearing, and descriptive feedback."""
    guess_center = feature_center(guess_feature)
    target_center = feature_center(target_feature)
    distance_km = haversine_km(guess_center, target_center)
    distance_miles = haversine_miles(guess_center, target_center)
    bearing_deg = initial_bearing(guess_center, target_center)
    compass = bearing_to_compass(bearing_deg)
    guess_iso = _feature_iso3(guess_feature)
    target_iso = _feature_iso3(target_feature)
    correct = bool(guess_iso and target_iso and guess_iso == target_iso)
    if not guess_iso or not target_iso:
        correct = _feature_name(guess_feature) == _feature_name(target_feature)

    return {
        "correct": correct,
        "guess_name": _feature_name(guess_feature),
        "target_name": _feature_name(target_feature),
        "guess_center": guess_center,
        "target_center": target_center,
        "distance_km": distance_km,
        "distance_miles": distance_miles,
        "bearing_deg": bearing_deg,
        "compass": compass,
        "arrow": ARROWS[compass],
    }


def format_feedback(result, units="km") -> str:
    """Pretty-print guess feedback."""
    if result["correct"]:
        return f"{result['guess_name']} is correct."

    if units == "miles":
        distance = result["distance_miles"]
        suffix = "mi"
    else:
        distance = result["distance_km"]
        suffix = "km"

    return (
        f"{result['guess_name']}: {result['arrow']} "
        f"{distance:,.0f} {suffix} toward {result['compass']}"
    )
