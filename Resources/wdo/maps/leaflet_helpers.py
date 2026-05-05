from ipyleaflet import (
    GeoJSON,
    LayersControl,
    Map,
    Marker,
    Polyline,
    Polygon,
    ScaleControl,
    basemaps,
)

from wdo.geometry.bbox import bbox_from_feature, bbox_from_features, bbox_to_polygon


def make_map(center=(0, 0), zoom=2, **kwargs):
    """Create and return a map object.

    Implement with folium or ipyleaflet depending on course choice.
    """
    kwargs.setdefault("scroll_wheel_zoom", True)
    kwargs.setdefault("basemap", basemaps.OpenStreetMap.Mapnik)
    return Map(center=center, zoom=zoom, **kwargs)


def map(center=(0, 0), zoom=2, **kwargs):
    return make_map(center=center, zoom=zoom, **kwargs)


def add_basemap(map_obj, name="OpenStreetMap"):
    """Add/select a basemap layer."""
    if name == "WorldImagery":
        map_obj.basemap = basemaps.Esri.WorldImagery
    elif name == "DarkMatter":
        map_obj.basemap = basemaps.CartoDB.DarkMatter
    else:
        map_obj.basemap = basemaps.OpenStreetMap.Mapnik
    return map_obj


def add_geojson(map_obj, data, name=None, style=None, **kwargs):
    """Add GeoJSON data to a map."""
    layer = GeoJSON(
        data=data,
        name=name or data.get("properties", {}).get("name", "GeoJSON"),
        style=style or {
            "color": "#2563eb",
            "fillColor": "#60a5fa",
            "weight": 2,
            "fillOpacity": 0.35,
        },
        **kwargs,
    )
    map_obj.add_layer(layer)
    return layer


def add_marker(map_obj, lat=None, lon=None, location=None, **kwargs):
    if location is None:
        location = (lat, lon)
    marker = Marker(location=location, **kwargs)
    map_obj.add_layer(marker)
    return marker


def fit_map_to_geojson(map_obj, data):
    """Adjust map viewport to fit GeoJSON bounds."""
    if data.get("type") == "FeatureCollection":
        bbox = bbox_from_features(data.get("features", []))
    elif data.get("type") == "Feature":
        bbox = bbox_from_feature(data)
    else:
        bbox = bbox_from_feature({"type": "Feature", "geometry": data, "properties": {}})

    min_lon, min_lat, max_lon, max_lat = bbox
    map_obj.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
    return bbox


def fit_bbox(map_obj, bbox):
    min_lon, min_lat, max_lon, max_lat = bbox
    map_obj.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
    return bbox


def add_layer_control(map_obj):
    """Add layer control widget."""
    control = LayersControl(position="topright")
    map_obj.add_control(control)
    return control


def add_scale_control(map_obj):
    """Add scale control widget."""
    control = ScaleControl(position="bottomleft")
    map_obj.add_control(control)
    return control


def add_bbox(map_obj, bbox, **style):
    """Draw a bounding box on the map."""
    defaults = {"color": "#ef4444", "fill_color": "#ef4444", "fill_opacity": 0.08}
    defaults.update(style)
    layer = Polygon(locations=bbox_to_polygon(bbox), **defaults)
    map_obj.add_layer(layer)
    return layer


def add_path(map_obj, coords, **style):
    """Add a path/polyline to the map."""
    defaults = {"color": "#111827", "weight": 3}
    defaults.update(style)
    layer = Polyline(locations=coords, **defaults)
    map_obj.add_layer(layer)
    return layer
