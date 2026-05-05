from dataclasses import dataclass
from math import asin, atan2, cos, degrees, radians, sin, sqrt


EARTH_RADIUS_KM = 6371.0088


@dataclass(frozen=True)
class LatLon:
    lat: float
    lon: float


def haversine_km(lat1, lon1, lat2, lon2):
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    return EARTH_RADIUS_KM * 2 * atan2(sqrt(a), sqrt(1 - a))


def initial_bearing_deg(lat1, lon1, lat2, lon2):
    phi1, phi2 = radians(lat1), radians(lat2)
    dlambda = radians(lon2 - lon1)
    y = sin(dlambda) * cos(phi2)
    x = cos(phi1) * sin(phi2) - sin(phi1) * cos(phi2) * cos(dlambda)
    return degrees(atan2(y, x)) % 360


def destination_point(lat, lon, bearing_deg, distance_km):
    angular = distance_km / EARTH_RADIUS_KM
    phi1 = radians(lat)
    lambda1 = radians(lon)
    theta = radians(bearing_deg)
    phi2 = asin(sin(phi1) * cos(angular) + cos(phi1) * sin(angular) * cos(theta))
    lambda2 = lambda1 + atan2(
        sin(theta) * sin(angular) * cos(phi1),
        cos(angular) - sin(phi1) * sin(phi2),
    )
    return LatLon(lat=degrees(phi2), lon=((degrees(lambda2) + 540) % 360) - 180)


def bbox_latlon(points):
    lats = [p.lat for p in points]
    lons = [p.lon for p in points]
    return [min(lons), min(lats), max(lons), max(lats)]


def _orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])


def _on_segment(p, q, r):
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])


def segments_intersect(p1, p2, p3, p4):
    d1 = _orientation(p1, p2, p3)
    d2 = _orientation(p1, p2, p4)
    d3 = _orientation(p3, p4, p1)
    d4 = _orientation(p3, p4, p2)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    if d1 == 0 and _on_segment(p1, p3, p2):
        return True
    if d2 == 0 and _on_segment(p1, p4, p2):
        return True
    if d3 == 0 and _on_segment(p3, p1, p4):
        return True
    if d4 == 0 and _on_segment(p3, p2, p4):
        return True
    return False


def point_in_polygon(point, polygon):
    lon, lat = point
    ring = polygon["coordinates"][0] if isinstance(polygon, dict) else polygon
    inside = False
    for i in range(len(ring) - 1):
        xi, yi = ring[i]
        xj, yj = ring[i + 1]
        if (yi > lat) != (yj > lat):
            x_intersect = xi + (lat - yi) * (xj - xi) / (yj - yi)
            if lon < x_intersect:
                inside = not inside
    return inside


def _merge_props(properties, props):
    if props:
        properties.update(props)
    return properties


def point_feature(*args, props=None, **properties):
    properties = _merge_props(properties, props)
    if len(args) == 1:
        point = args[0]
        coord = [point.lon, point.lat] if isinstance(point, LatLon) else list(point)
    elif len(args) == 2:
        coord = [args[0], args[1]]
    elif len(args) == 3 and isinstance(args[2], dict):
        coord = [args[0], args[1]]
        properties.update(args[2])
    else:
        raise TypeError("point_feature expects a point, lon/lat, or lon/lat/properties")
    return {"type": "Feature", "properties": properties, "geometry": {"type": "Point", "coordinates": coord}}


def line_feature(coords, props=None, **properties):
    properties = _merge_props(properties, props)
    out = [[p.lon, p.lat] if isinstance(p, LatLon) else list(p) for p in coords]
    return {"type": "Feature", "properties": properties, "geometry": {"type": "LineString", "coordinates": out}}


def polygon_feature(ring, props=None, **properties):
    properties = _merge_props(properties, props)
    out = [[p.lon, p.lat] if isinstance(p, LatLon) else list(p) for p in ring]
    if out[0] != out[-1]:
        out.append(out[0])
    return {"type": "Feature", "properties": properties, "geometry": {"type": "Polygon", "coordinates": [out]}}


def feature_collection(features):
    return {"type": "FeatureCollection", "features": list(features)}
