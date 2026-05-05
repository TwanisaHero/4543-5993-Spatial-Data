import json
from pathlib import Path

from ipyleaflet import Icon, LayersControl, Map, Marker, WidgetControl
import ipywidgets as widgets


class GeoJsonHelp:
    """Small helper for loading and inspecting GeoJSON files."""

    def __init__(self, path: Path = None):
        self.geojson_obj = None
        self.path = path
        if path:
            self.load_geojson(path)

    def load_geojson(self, path: Path):
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"GeoJSON file not found: {path}")
        self.path = path
        self.geojson_obj = json.loads(path.read_text(encoding="utf-8"))
        return self.geojson_obj

    def feature_count(self):
        if not self.geojson_obj:
            return 0
        return len(self.geojson_obj.get("features", []))

    def geometry_types(self):
        if not self.geojson_obj:
            return []
        return sorted(
            {
                feature.get("geometry", {}).get("type", "Unknown")
                for feature in self.geojson_obj.get("features", [])
            }
        )


class ClickMapApp:
    """Reusable ipyleaflet click-capture map."""

    def __init__(self, outfile="../data/clicked_points.json", center=(40.0, -99.0), zoom=5):
        self.outfile = Path(outfile)
        self.clicked_points = []
        self.markers = []
        if self.outfile.exists():
            self.clicked_points = json.loads(self.outfile.read_text(encoding="utf-8"))

        self.map = Map(
            center=center,
            zoom=zoom,
            layout=widgets.Layout(width="100%", height="700px"),
        )
        self.map.add(LayersControl())
        self.output = widgets.Output()
        self.clear_btn = widgets.Button(description="Clear Saved Points")
        self.clear_btn.on_click(self.clear)
        self.map.on_interaction(self.handle_interaction)
        self.map.add(WidgetControl(widget=self.clear_btn, position="topright"))
        self.map.add(WidgetControl(widget=self.output, position="bottomleft"))
        self.restore_markers()

    def save_points(self):
        self.outfile.parent.mkdir(parents=True, exist_ok=True)
        self.outfile.write_text(json.dumps(self.clicked_points, indent=2), encoding="utf-8")

    def marker_icon(self):
        icon_path = Path("../data/flag_icon.svg")
        if icon_path.exists():
            return Icon(icon_url=str(icon_path), icon_size=[30, 30])
        return None

    def add_marker(self, lat, lon):
        icon = self.marker_icon()
        marker = Marker(location=(lat, lon), icon=icon) if icon else Marker(location=(lat, lon))
        self.markers.append(marker)
        self.map.add(marker)
        return marker

    def restore_markers(self):
        for point in self.clicked_points:
            self.add_marker(point["lat"], point["lon"])

    def handle_interaction(self, **kwargs):
        if kwargs.get("type") != "click":
            return
        lat, lon = kwargs["coordinates"]
        point = {"lat": round(lat, 6), "lon": round(lon, 6)}
        self.clicked_points.append(point)
        self.add_marker(point["lat"], point["lon"])
        self.save_points()
        with self.output:
            print(point)

    def clear(self, _=None):
        for marker in self.markers:
            self.map.remove(marker)
        self.markers.clear()
        self.clicked_points.clear()
        self.save_points()
        self.output.clear_output()
