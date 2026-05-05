def bbox_from_points(points):
    """Return bbox as (min_lon, min_lat, max_lon, max_lat)."""
    lats = [p[0] for p in points]
    lons = [p[1] for p in points]
    return (min(lons), min(lats), max(lons), max(lats))


def _iter_lon_lat(coords):
    """Yield ``(lon, lat)`` pairs from nested GeoJSON coordinates."""
    if not coords:
        return
    first = coords[0]
    if isinstance(first, (int, float)) and len(coords) >= 2:
        yield (coords[0], coords[1])
        return
    for item in coords:
        yield from _iter_lon_lat(item)


def bbox_from_feature(feature):
    """Extract all coordinates from a feature and compute bbox."""
    geometry = feature.get("geometry", {}) if feature else {}
    coords = geometry.get("coordinates", [])
    points = list(_iter_lon_lat(coords))
    if not points:
        raise ValueError("Feature has no coordinates")

    lons = [point[0] for point in points]
    lats = [point[1] for point in points]
    return (min(lons), min(lats), max(lons), max(lats))


def bbox_from_features(features):
    """Compute bbox across multiple features."""
    boxes = [bbox_from_feature(feature) for feature in features]
    if not boxes:
        raise ValueError("No features supplied")

    min_lons, min_lats, max_lons, max_lats = zip(*boxes)
    return (min(min_lons), min(min_lats), max(max_lons), max(max_lats))


def bbox_to_polygon(bbox):
    """Convert bbox tuple into a closed polygon coordinate list."""
    min_lon, min_lat, max_lon, max_lat = bbox
    return [
        (min_lat, min_lon),
        (min_lat, max_lon),
        (max_lat, max_lon),
        (max_lat, min_lon),
        (min_lat, min_lon),
    ]
