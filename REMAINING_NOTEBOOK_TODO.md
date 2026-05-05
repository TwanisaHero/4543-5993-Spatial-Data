# Remaining Notebook TODO Inventory


## Assignments\02-Missile_Geometry_202


### Assignments\02-Missile_Geometry_202\_micro_lessons\00-Paths\00-Working_Directory.ipynb

- Cell 6
  - Prompt: ## Exercise B  List the contents of the *parent* directory — one level above where Python is running.  Use `.parent` on `Path.cwd()` and call `.iterdir()` on the result.
  - Source: `from pathlib import Path |  | # List the items one level up from cwd | # Your code here`

- Cell 8
  - Prompt: ## Exercise C  Without running any code, predict what absolute path Python would try to open if you wrote:  ```python Path("data/countries.geojson") ```  Then write a one-liner to confirm your prediction.
  - Source: `from pathlib import Path |  | # Confirm what Path("data/countries.geojson") would resolve to | # Your code here`

- Cell 10
  - Prompt: ## Optional Advanced — Changing the Working Directory  `os.chdir()` can change the working directory mid-notebook.  1. Change to the parent directory using `os.chdir(Path.cwd().parent)` 2. Print the new `Path.cwd()` 3. Change back to the original  Then answer: what risks does calling `os.chdir()` mid-notebook introduce for other cells?
  - Source: `import os | from pathlib import Path |  | original = Path.cwd() |  | # 1. Change to the parent directory | # 2. Print the new cwd | # 3. Change back to original | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\00-Paths\01-Relative_vs_Absolute.ipynb

- Cell 9
  - Prompt: ## Exercise C  You are given this relative path: `"../data/countries.geojson"`  1. Resolve it to an absolute path using `.resolve()` 2. Print the result 3. In a comment, explain what `..` means
  - Source: `from pathlib import Path |  | # Given this relative path with ".." components: | p = Path("../data/countries.geojson") |  | # 1. Resolve it to an absolute path | # 2. Print the result | # 3. What does the ".." mean in this context? | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\00-Paths\02-Data_Elsewhere.ipynb

- Cell 7
  - Prompt: ## Exercise B  The `data/` folder doesn't live inside `00-Paths/` — it's one level up from here.  Fix the path in the cell below so that `exists()` returns `True`.
  - Source: `from pathlib import Path |  | # The data folder lives one level above 00-Paths/. | # Fix the path below so that exists() returns True for countries.geojson. | data_file = Path("???/countries.geojson") |  | print("Path:", data_file) | print("Exists:", data_file.exists())`

- Cell 11
  - Prompt: ## Optional Advanced — Set Up a Local Workspace  Use `pathlib` (no shell commands) to:  1. Create a `data/` folder inside `00-Paths/` using `Path.mkdir(exist_ok=True)` 2. Create an `output/` folder the same way 3. Copy one json file from the module's data folder into your new local `data/` using `shutil.copy2` 4. Re-run the existence check from above and confirm all three paths are found  Hint: `Path.mkdir(parents=True, exist_ok=True)` will not error if the folder already exists.
  - Source: `from pathlib import Path |  | # Create a local data/ and output/ folder inside 00-Paths/ if they don't exist | # Then copy one json file from the module data folder into data/ | # Finally, re-run the existence check from above to confirm everything is found |  | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\00-Paths\03-Find_Project_Root.ipynb

- Cell 8
  - Prompt: ## Exercise B  Call `find_project_root()` with a different marker.  1. Try `"pyproject.toml"` — does it find a root? What does that tell you? 2. Try a marker that definitely doesn't exist (e.g. `"banana"`) — what happens, and why is the `RuntimeError` message useful?
  - Source: `from pathlib import Path |  | # Change the marker to "pyproject.toml" and test what happens. | # Then try a marker that definitely doesn't exist (e.g. "banana"). | # Your code here`

- Cell 10
  - Prompt: ## Exercise C  Use `find_project_root()` to build a reliable path to this module's `countries.geojson` data file.  Use the directory tree printed above to figure out the correct subfolders from root, then replace `"???"` in the cell below.
  - Source: `from pathlib import Path |  | root = find_project_root() |  | # Build the path from root to this module's data folder and check countries.geojson | # Hint: look at the directory tree printed above to figure out the right subfolders | data_file = root / "???" / "countries.geojson" |  | print("Looking for:", data_file) | print("Exists:", data_file.exists())`

- Cell 12
  - Prompt: ## Optional Advanced — Multiple Markers and Custom Start  Extend `find_project_root` to accept:  - `markers` — a list of marker names; stop at the first directory that contains **any** of them - `start` — an optional starting path (defaults to `Path.cwd()` if not given)  This lets you test the function from any location and makes it more flexible for projects that don't use git.
  - Source: `from pathlib import Path |  | def find_project_root_multi(markers=(".git", "pyproject.toml", "setup.py"), start: Path = None): |     """Return the first ancestor directory that contains any of the marker files/folders.""" |     # Your code here |     pass |  | root = find_project_root_multi() | print("Root:", root)`


### Assignments\02-Missile_Geometry_202\_micro_lessons\01-JSON_GeoJSON\00-Reading_JSON.ipynb

- Cell 14
  - Prompt: ## Exercise A  Count how many color entries have a red channel (`rgb[0]`) greater than `200`. Skip empty entries.
  - Source: `# Count how many color entries have a red channel (rgb[0]) greater than 200 | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Build a list of `(name, brightness)` tuples for every color, where brightness is the sum of its `rgb` values. Print the **5 brightest** colors, sorted from highest to lowest.
  - Source: `# Build a sorted list of (name, brightness) for the top 5 brightest colors | # brightness = sum of the rgb list | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\01-JSON_GeoJSON\01-GeoJSON_Structure.ipynb

- Cell 16
  - Prompt: ## Exercise A  How many meteorites in this dataset have a recorded mass (non-`None`, non-zero)?  Use `.get("mass")` to safely access the field — some features may not have it.
  - Source: `features = data["features"] |  | # Count how many features have a non-None, non-zero mass value | # Your code here`

- Cell 18
  - Prompt: ## Exercise B  Find all meteorites that fell **after the year 2000**. Print their names and years.  Use `.get("year")` with a default since some entries may be missing that field.
  - Source: `features = data["features"] |  | # Find all meteorites that fell after year 2000 | # Print their names and years | # Your code here`

- Cell 20
  - Prompt: ## Exercise C  Find the **3 northernmost** meteorites — those with the highest latitude. Print their names and latitudes, sorted from north to south.  Hint: latitude is `coordinates[1]`.
  - Source: `features = data["features"] |  | # Find the 3 northernmost meteorites — highest latitude (index 1 of coordinates) | # Sort and print their names and latitudes | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\01-JSON_GeoJSON\02-Feature_Collections.ipynb

- Cell 19
  - Prompt: ## Exercise B  Write a function `count_coordinates(feature) -> int` that returns the total number of coordinate pairs in any feature — it must handle `Point`, `LineString`, and `Polygon` geometry types.  Test it by printing the coordinate count for each feature in the collection.
  - Source: `def count_coordinates(feature) -> int: |     """Return the total number of coordinate pairs in a feature, regardless of geometry type.""" |     # Your code here |     pass |  | for f in collection["features"]: |     name = f["properties"]["name"] |     geom_type = f["geometry"]["type"] |     print(f"{geom_type:<16} {name:<30} coords: {count_coordinates(f)}")`

- Cell 21
  - Prompt: ## Exercise C  Load `meteorites.geojson`, filter to only meteorites with `mass > 50000`, and save the result as a new `FeatureCollection` to `data/heavy_meteorites.geojson`. Print how many passed the filter.
  - Source: `import json | from pathlib import Path |  | meteorites = json.loads(Path("data/meteorites.geojson").read_text()) |  | # Filter to meteorites with mass > 50000 | # Save the result as a new FeatureCollection to data/heavy_meteorites.geojson | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\02-Viewing_GeoJSON\01-iPyLeaflet_Intro.ipynb

- Cell 17
  - Prompt: ## Exercise A  Pick 3 US cities you know. Look up their `(lat, lon)` coordinates and add a default `Marker` for each — with `title` set to the city name — on a zoom-5 map centered roughly over the US.
  - Source: `from ipyleaflet import Map, Marker |  | # Pick 3 US cities you know. Look up their (lat, lon) coordinates. | # Add a default Marker for each with a title set to the city name. | # Center the map at zoom 5 so all three are visible. | # Your code here`

- Cell 19
  - Prompt: ## Exercise B  Take one of your markers from Exercise A and attach a `Popup` using `ipywidgets.HTML`. The popup should display the city name and one fact (population, founding year, or elevation) when clicked.
  - Source: `from ipyleaflet import Map, Marker | from ipywidgets import HTML |  | # Build on Exercise A — attach a popup to one of your markers | # The popup should show the city name and one fact (population, elevation, or founding year) | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\02-Viewing_GeoJSON\02-Add_GeoJSON.ipynb

- Cell 15
  - Prompt: ## Exercise A  Load `data/meteorites.geojson` and display all features as a single `GeoJSON` layer on a world-scale map (`center=(20, 0)`, `zoom=2`).
  - Source: `import json | from ipyleaflet import Map, GeoJSON |  | with open("data/meteorites.geojson") as f: |     meteorites = json.load(f) |  | # Display all meteorite features as a single GeoJSON layer on a world map | # center=(20, 0), zoom=2 | # Your code here`

- Cell 17
  - Prompt: ## Exercise B  Using `data/wichita_falls.geojson`:  1. Print the count of features for each geometry type 2. Display all features on one map with each geometry type as a **separate named layer**
  - Source: `import json | from ipyleaflet import Map, GeoJSON |  | with open("data/wichita_falls.geojson") as f: |     features = json.load(f)["features"] |  | # Count features per geometry type, then display all on one map with each type as a separate named layer | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\02-Viewing_GeoJSON\03-Map_Control.ipynb

- Cell 17
  - Prompt: ## Exercise A  Rebuild the "Putting It Together" map using `basemaps.Esri.WorldImagery` (satellite tiles) instead of the default street map. Keep all three named layers and all four controls.
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, ScaleControl, FullscreenControl, MiniMap |  | # Rebuild the composite map — polygon layer starts hidden (visible=False) | m = Map(center=WICHITA_FALLS, zoom=12) |  | poly_layer = GeoJSON(data=make_fc(polygons), name="Park Boundary", visible=False) |  | # Add the remaining layers and all four controls | # Your code here |  | m`

- Cell 19
  - Prompt: ## Exercise B  ipyleaflet layers have a `visible` attribute you can set at any time — the map updates live without re-rendering.  1. Rebuild the composite map with the polygon layer starting **hidden** (`visible=False`) 2. Display the map — confirm the polygon layer is absent 3. In a new cell, set `poly_layer.visible = True` and watch the map update in place
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, ScaleControl, FullscreenControl, MiniMap, basemaps |  | m = Map(center=WICHITA_FALLS, zoom=12, basemap=basemaps.Esri.WorldImagery) |  | # Add the three named layers and all four controls | # Your code here |  | m`


### Assignments\02-Missile_Geometry_202\_micro_lessons\03-Attributes_Styling_Filtering\00-Properties.ipynb

- Cell 22
  - Prompt: ## Exercise A  Build a dict that maps each feature `type` to a list of feature names with that type.  Expected shape: `{"park": ["Lucy Park", ...], "water": [...], ...}`
  - Source: `from collections import defaultdict |  | # Build a dict mapping each feature type to a list of names | # e.g. {"park": ["Lucy Park", ...], "water": [...], ...} | # Your code here`

- Cell 24
  - Prompt: ## Exercise B  Add a new property `"label"` to every feature in `geojson["features"]`, formatted as `"{type}: {name}"` (e.g. `"park: Lucy Park"`). Print the first three labels to confirm.
  - Source: `# Add a "label" property to every feature formatted as "{type}: {name}" | # Print the first 3 labels to confirm | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\03-Attributes_Styling_Filtering\01-Style_Functions.ipynb

- Cell 22
  - Prompt: ## Exercise A  Write a style function that colors features by **geometry type** rather than by the `type` property:  | Geometry | Color | |---|---| | `Point` | red `#e74c3c` | | `LineString` | orange `#e67e22` | | `Polygon` | blue `#2980b9` |  Display `wichita_falls.geojson` with this function.
  - Source: `from ipyleaflet import Map, GeoJSON |  | # Style by geometry type: Points=red, LineStrings=orange, Polygons=blue | def style_by_geom(feature): |     # Your code here |     pass |  | m = Map(center=WICHITA_FALLS, zoom=12) | m.add(GeoJSON(data=geojson, style=style_by_geom)) | m`

- Cell 24
  - Prompt: ## Exercise C  Extend the numeric style function to use **4 color levels** instead of 3:  | Score | Color | |---|---| | `>= 75` | red `#e74c3c` | | `50–74` | orange `#e67e22` | | `25–49` | yellow `#f1c40f` | | `< 25` | blue `#3498db` |  Apply it to the `scored` dataset from the teaching cells.
  - Source: `def style_by_score_4(feature): |     """4-level color scale: < 25, 25–49, 50–74, >= 75""" |     # Your code here |     pass |  | m = Map(center=WICHITA_FALLS, zoom=12) | m.add(GeoJSON(data=scored, style=style_by_score_4)) | m`


### Assignments\02-Missile_Geometry_202\_micro_lessons\03-Attributes_Styling_Filtering\02-Filtering.ipynb

- Cell 21
  - Prompt: ## Exercise A  Filter `wichita_falls.geojson` to show only `Polygon` and `LineString` features (exclude all `Point` features). Apply `style_by_type` from the teaching cells and display the result.
  - Source: `from ipyleaflet import Map, GeoJSON |  | COLOR_MAP = { |     "park":       "#2ecc71", |     "water":      "#1abc9c", |     "education":  "#3498db", |     "government": "#e74c3c", |     "route":      "#e67e22", | } |  | def style_by_type(feature): |     color = COLOR_MAP.get(feature["properties"].get("type"), "#95a5a6") |     return {"color": color, "fillColor": color, "fillOpacity": 0.5, "weight": 2} |  | # Filter to only Polygon and LineString features (exclude Points) | # Apply style_by_type and display | # Your code here`

- Cell 23
  - Prompt: ## Exercise B  Load `meteorites.geojson` (hint: it's two levels up in `data/`). Filter to meteorites where **mass > 10000 and year is recorded** (not `None` or `0`). Display them on a world map and print the count.
  - Source: `import json | from ipyleaflet import Map, GeoJSON |  | with open("../../data/meteorites.geojson") as f: |     meteorites = json.load(f) |  | # Filter: mass > 10000 AND year is not None/0 | # Display on a world map (center=(20, 0), zoom=2), print the count | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\04-Interactive_Maps\00-Map_Events.ipynb

- Cell 17
  - Prompt: ## Exercise A  Modify the click handler to only place a marker on **every other click** — odd-numbered clicks (1st, 3rd, 5th...) get a marker; even-numbered clicks are silently ignored. Print which clicks are skipped.
  - Source: `from ipyleaflet import Map, Marker |  | m = Map(center=WICHITA_FALLS, zoom=12) | markers = [] |  | # Modify the handler to only place a marker on every OTHER click (1st, 3rd, 5th...) | # Even-numbered clicks are silently ignored | # Your code here |  | m`

- Cell 19
  - Prompt: ## Exercise B  Extend your click handler to handle two event types:  - **Single click** (`"click"`) — drops a default marker - **Double-click** (`"dblclick"`) — removes all markers from the map and prints `"Cleared"`  Tip: check `kwargs.get("type")` for both values.
  - Source: `from ipyleaflet import Map, Marker, AwesomeIcon |  | m = Map(center=WICHITA_FALLS, zoom=12) |  | # Single click → default blue marker | # Double-click ("dblclick") → clear all markers | # Your code here |  | m`


### Assignments\02-Missile_Geometry_202\_micro_lessons\04-Interactive_Maps\01-Click_Interactions.ipynb

- Cell 19
  - Prompt: ## Exercise A  Click the `build_path` map above to collect at least 3 points. Then, in the cell below, convert `path_points` into a single **`LineString`** GeoJSON feature (not a FeatureCollection of Points). Print the result.  Remember: GeoJSON coordinate order is `[lon, lat]`.
  - Source: `import json |  | # After clicking the map above to collect path_points, run this cell. | # Convert path_points into a single LineString GeoJSON feature (not a collection of Points). | # Print the result. | # Your code here`

- Cell 21
  - Prompt: ## Exercise B  Add an **Undo** button to the live path builder. Each click of the button should:  1. Remove the last marker from the map 2. Pop the last entry from the points list 3. Update the `Polyline` to reflect the shorter path
  - Source: `from ipyleaflet import Map, Marker, Polyline | from ipywidgets import Button, HBox, VBox |  | m = Map(center=WICHITA_FALLS, zoom=12) |  | undo_points = [] | undo_markers = [] | undo_line = Polyline(locations=[], color="#e74c3c", weight=3) | m.add(undo_line) |  | # Add an "Undo" button that removes the last marker and pops the last point | # Update the polyline after each undo | # Your code here |  | m`


### Assignments\02-Missile_Geometry_202\_micro_lessons\04-Interactive_Maps\02-Dynamic_Layers.ipynb

- Cell 25
  - Prompt: ## Exercise B  Build a button panel with one `Button` per feature type (park, water, education, government, route). Clicking a button calls `show_only()` to display only that layer. Below the map, an `Output` widget updates to show which layer is currently visible.
  - Source: `from ipywidgets import Button, HBox, VBox, Output |  | m2 = Map(center=WICHITA_FALLS, zoom=12) | for layer in layers.values(): |     m2.add(layer) |  | layer_status = Output(layout={"border": "1px solid #ccc", "padding": "6px"}) |  | # Build one Button per feature type; clicking it calls show_only(m2, layers, type_name) | # After each click, update layer_status to show which layers are currently visible | # Your code here |  | VBox([m2, layer_status])`


### Assignments\02-Missile_Geometry_202\_micro_lessons\04-Interactive_Maps\03-User_Feedback.ipynb

- Cell 19
  - Prompt: ## Exercise A  Extend the two-click line tool from the teaching cells to also place a **midpoint marker** between Point A and Point B.  - Midpoint formula: `((lat1+lat2)/2, (lon1+lon2)/2)` - Style it differently from the endpoint markers (use an `AwesomeIcon` with a different color or icon) - Display the distance in the status panel as before
  - Source: `import math | from ipyleaflet import Map, Marker, Polyline | from ipywidgets import HTML, Output, VBox |  | def haversine_km(lat1, lon1, lat2, lon2): |     R = 6371 |     dlat, dlon = math.radians(lat2-lat1), math.radians(lon2-lon1) |     a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2 |     return R * 2 * math.asin(math.sqrt(a)) |  | m = Map(center=WICHITA_FALLS, zoom=12) | status = Output(layout={"border": "1px solid #ccc", "padding": "6px"}) |  | points = [] | line = Polyline(locations=[], color="#8e44ad", weight=3) | m.add(line) |  | # Extend the two-click line tool to also place a midpoint marker | # Midpoint: ((lat1+lat2)/2, (lon1+lon2)/2) | # Display it with a different AwesomeIcon to distinguish it from the endpoints | # Your code here |  | m.on_interaction(on_click) | VBox([m, status])`

- Cell 21
  - Prompt: ## Exercise B  Build a click counter using a `Label` widget:  - Every click increments the counter and updates the label (e.g. `"Clicks: 4"`) - Each click also adds a marker to the map - A **Reset** button zeroes the counter, updates the label, and removes all placed markers
  - Source: `from ipyleaflet import Map, Marker | from ipywidgets import Label, Button, HBox, VBox |  | m = Map(center=WICHITA_FALLS, zoom=12) |  | counter = [0] | counter_label = Label(value="Clicks: 0") | placed = [] |  | # Each click increments counter_label and adds a marker | # "Reset" button zeroes the counter and removes all markers | # Your code here |  | reset_btn = Button(description="Reset", button_style="danger") | VBox([m, HBox([counter_label, reset_btn])])`


### Assignments\02-Missile_Geometry_202\_micro_lessons\05-Coordinate_Geometry\00-Coordinate_Ranges.ipynb

- Cell 14
  - Prompt: ---  ## Exercise A — Label Each Coordinate Pair  For each pair below, determine whether it is **valid**, **invalid** (out of range), or **suspiciously swapped**.  ```python pairs = [     [-87.6,  41.8],   # Chicago     [41.8,  -87.6],   # ?     [180.1,  22.0],   # ?     [-73.9,  40.7],   # New York     [-90.0, -91.0],   # ?     [0.0,    0.0],    # ? ] ```  Write a loop that prints a label for each one.
  - Source: `pairs = [ |     [-87.6,  41.8], |     [41.8,  -87.6], |     [180.1,  22.0], |     [-73.9,  40.7], |     [-90.0, -91.0], |     [0.0,    0.0], | ] |  | # your code here`

- Cell 16
  - Prompt: ## Exercise B — Compass Extremes from a Feature Collection  Given the feature collection below, print the four compass extremes: westernmost, easternmost, southernmost, northernmost longitude/latitude values.
  - Source: `fc = { |     "type": "FeatureCollection", |     "features": [ |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.2, 34.1]}, "properties": {}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-99.0, 32.9]}, "properties": {}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98.1, 33.4]}, "properties": {}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.8, 34.6]}, "properties": {}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98.5, 33.8]}, "properties": {}}, |     ] | } |  | # your code here | # expected output: | #   Westernmost: -99.0 | #   Easternmost: -97.2 | #   Southernmost: 32.9 | #   Northernmost: 34.6`

- Cell 18
  - Prompt: ## Exercise C — Scan and Report Invalid Coordinates  The list below contains some coordinate pairs with errors. Write a function `scan_for_errors(coords)` that returns only the pairs that fail validity checks, along with a description of what is wrong.
  - Source: `mixed_bag = [ |     [-98.5,  33.8], |     [-200.0, 45.0], |     [0.0,    91.5], |     [-73.9,  40.7], |     [33.8,  -98.5], |     [-97.0,  35.2], |     [181.0,  22.0], | ] |  | def scan_for_errors(coords): |     # your code here |     pass |  | errors = scan_for_errors(mixed_bag) | for e in errors: |     print(e)`


### Assignments\02-Missile_Geometry_202\_micro_lessons\05-Coordinate_Geometry\01-Compute_BBox.ipynb

- Cell 16
  - Prompt: ---  ## Exercise A — Compute BBox Manually, Then Verify with Python  Given the coordinates below, first determine the bounding box by eye, then compute it with Python and confirm.  ```python coords = [     [-104.9, 39.7],   # Denver     [-118.2, 34.0],   # Los Angeles     [-87.6,  41.8],   # Chicago     [-73.9,  40.7],   # New York     [-122.4, 37.7],   # San Francisco ] ```  What do you expect `min_lon`, `max_lon`, `min_lat`, `max_lat` to be before running the code?
  - Source: `coords = [ |     [-104.9, 39.7], |     [-118.2, 34.0], |     [-87.6,  41.8], |     [-73.9,  40.7], |     [-122.4, 37.7], | ] |  | # your code here`

- Cell 18
  - Prompt: ## Exercise B — BBox from a GeoJSON FeatureCollection  Read the feature collection below and compute the bbox for **all Point features** using `compute_bbox` and `extract_point_coords`. Then validate it with `validate_bbox`.
  - Source: `airfields = { |     "type": "FeatureCollection", |     "features": [ |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.37, 35.39]}, "properties": {"name": "Tinker AFB"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-94.37, 35.34]}, "properties": {"name": "Fort Smith Regional"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-101.70, 33.66]}, "properties": {"name": "Lubbock Preston Smith"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.04, 32.85]}, "properties": {"name": "NAS Fort Worth JRB"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98.47, 29.53]}, "properties": {"name": "Kelly Field Annex"}}, |     ] | } |  | # your code here`

- Cell 20
  - Prompt: ## Exercise C — Per-Feature BBox Comparison  Compute a separate bbox for each feature in `airfields` and print each one. Which feature has the largest longitude span? (Hint: for Point features the bbox degenerates to a single point — that is expected.)
  - Source: `# your code here | # for each feature, compute and print: | #   feature name, bbox, and lon/lat span`

- Cell 22
  - Prompt: ## Exercise D — Write `compute_bbox(points)` from Scratch  Without looking back at the earlier implementation, write `compute_bbox` again from scratch. Then test it on at least two different datasets — one point collection and one polygon's exterior ring.
  - Source: `def compute_bbox(coords): |     # your code here |     pass |  |  | # Test 1: point collection | test_points = [[-98.5, 33.8], [-97.2, 34.1], [-99.0, 32.9]] | print(compute_bbox(test_points))   # expected: [-99.0, 32.9, -97.2, 34.1] |  | # Test 2: polygon exterior ring | test_ring = [[-99.0, 33.5], [-97.2, 33.5], [-97.2, 34.8], [-99.0, 34.8], [-99.0, 33.5]] | print(compute_bbox(test_ring))     # expected: [-99.0, 33.5, -97.2, 34.8]`


### Assignments\02-Missile_Geometry_202\_micro_lessons\05-Coordinate_Geometry\02-Draw_BBox.ipynb

- Cell 16
  - Prompt: ---  ## Exercise A — Compute and Draw from Point Data  Given the airfield coordinates below, compute the bbox and draw it on a map alongside the original points. Use a styled bbox layer that is clearly distinct from the point markers.
  - Source: `airfields_fc = { |     "type": "FeatureCollection", |     "features": [ |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.37, 35.39]}, "properties": {"name": "Tinker AFB"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-94.37, 35.34]}, "properties": {"name": "Fort Smith Regional"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-101.70, 33.66]}, "properties": {"name": "Lubbock Preston Smith"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.04, 32.85]}, "properties": {"name": "NAS Fort Worth JRB"}}, |         {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98.47, 29.53]}, "properties": {"name": "Kelly Field Annex"}}, |     ] | } |  | # your code here | # 1. extract coordinates | # 2. compute bbox with compute_bbox() | # 3. build bbox polygon with `

- Cell 18
  - Prompt: ## Exercise B — Overlay Polygon and Its BBox  Draw the irregular polygon from Section 6 and its bbox on the same map. Use different colors for each. How much empty space is inside the bbox but outside the polygon?
  - Source: `# irregular_fc and poly_bbox are already defined above | # your code here — two styled layers on one map`

- Cell 20
  - Prompt: ## Exercise C — Multi-Feature BBox Layers  For each airfield in `airfields_fc`, draw its individual bbox (a degenerate rectangle for a point — same coordinates on all four corners) using a distinct color per feature. All five bboxes should appear on a single map alongside the points.
  - Source: `colors = ["#e63946", "#2a9d8f", "#e9c46a", "#f4a261", "#264653"] |  | # your code here | # hint: loop over features, compute individual bbox, add a styled GeoJSON layer per feature`

- Cell 22
  - Prompt: ## Exercise D — Fit the Map to the Data  Using `airfields_fc` and its bbox, display the map using `fit_bounds` rather than a hardcoded center and zoom. Confirm that all points are visible without manual adjustment.
  - Source: `# your code here | # use bbox_to_map_bounds() and m.fit_bounds()`


### Assignments\02-Missile_Geometry_202\_micro_lessons\05-Coordinate_Geometry\03-Why_LatLon_Is_Weird.ipynb

- Cell 18
  - Prompt: ## Exercise B — One Degree of Longitude Across Latitudes  Using `km_per_degree_lon`, compute the approximate ground distance covered by one degree of longitude at every 10° of latitude from 0° to 80°. Print the results as a table.
  - Source: `# your code here | # hint: range(0, 81, 10)`


### Assignments\02-Missile_Geometry_202\_micro_lessons\06-Distance\00-Euclidean_Distance.ipynb

- Cell 10
  - Prompt: ---  ## Exercise A — Distances Between Several Points  Compute the Euclidean distance from the base point to each of the targets below. Print the results sorted nearest to farthest.
  - Source: `base = (-98.47, 33.91)   # Wichita Falls area |  | targets = [ |     ("Tinker AFB",         (-97.37, 35.39)), |     ("NAS Fort Worth JRB", (-97.04, 32.85)), |     ("Lubbock",            (-101.87, 33.57)), |     ("Oklahoma City",      (-97.52, 35.47)), |     ("Abilene",            (-99.73, 32.45)), | ] |  | # your code here | # expected: sorted list of (name, euclidean_distance) from nearest to farthest`

- Cell 12
  - Prompt: ## Exercise B — Rank Nearest Points  Using `euclidean_distance`, write a function `nearest_n(base, points, n)` that returns the `n` closest points from a list, sorted by distance. Test it on the targets above.
  - Source: `def nearest_n(base, named_points, n): |     """ |     Returns the n closest (name, coord) pairs from named_points to base, |     sorted nearest first. |     named_points: list of (name, (lon, lat)) |     """ |     # your code here |     pass |  |  | top3 = nearest_n(base, targets, 3) | for name, coord in top3: |     print(f"{name}: {euclidean_distance(base, coord):.4f}°")`

- Cell 14
  - Prompt: ## Exercise C — Visualize All Distances  Plot `base` and all five targets on a map. Draw a line from `base` to each target. Label each line with the Euclidean distance value (in the `properties` dict — you can inspect it in the browser dev tools or just print it before displaying).
  - Source: `# your code here | # build a FeatureCollection with: | #   - one Point feature for base | #   - one Point feature per target | #   - one LineString per target (base → target), with distance in properties`


### Assignments\02-Missile_Geometry_202\_micro_lessons\06-Distance\01-Haversine_Distance.ipynb

- Cell 13
  - Prompt: ---  ## Exercise A — Distances Between Cities  Compute the Haversine distance between each pair of cities below. Print the results in a readable table.
  - Source: `city_pairs = [ |     ("Wichita Falls → Dallas",     (-98.49, 33.91), (-96.80, 32.78)), |     ("Dallas → San Antonio",       (-96.80, 32.78), (-98.49, 29.42)), |     ("OKC → Tulsa",                (-97.52, 35.47), (-95.99, 36.15)), |     ("Lubbock → Amarillo",         (-101.87, 33.57), (-101.83, 35.22)), |     ("El Paso → Dallas",           (-106.49, 31.76), (-96.80, 32.78)), | ] |  | # your code here | # print each pair name and Haversine distance in km`

- Cell 15
  - Prompt: ## Exercise B — Nearest Airfield by Real Distance  Using `haversine_km`, find the nearest airfield to the base point. Compare your answer to the Euclidean ranking from the previous notebook — does the order change?
  - Source: `base = (-98.47, 33.91) |  | airfields = [ |     ("Tinker AFB",         (-97.37, 35.39)), |     ("NAS Fort Worth JRB", (-97.04, 32.85)), |     ("Lubbock",            (-101.87, 33.57)), |     ("Oklahoma City",      (-97.52, 35.47)), |     ("Abilene",            (-99.73, 32.45)), | ] |  | # your code here | # print airfields sorted by haversine_km distance, nearest first`


### Assignments\02-Missile_Geometry_202\_micro_lessons\06-Distance\02-Compare_Methods.ipynb

- Cell 13
  - Prompt: ---  ## Exercise A — Compute Percentage Error  For each pair below, compute the Euclidean distance in degrees, convert it to an approximate km estimate using `111.32 km/°`, and compute the percentage error against the Haversine result. Print a table sorted by error, largest to smallest.
  - Source: `exercise_pairs = [ |     ("Tinker AFB → NAS Fort Worth",  (-97.37, 35.39), (-97.04, 32.85)), |     ("Dallas → Chicago",             (-96.80, 32.78), (-87.63, 41.88)), |     ("Dallas → Mexico City",         (-96.80, 32.78), (-99.13, 19.43)), |     ("OKC → Tulsa",                  (-97.52, 35.47), (-95.99, 36.15)), |     ("Dallas → Buenos Aires",        (-96.80, 32.78), (-58.38, -34.61)), |     ("Wichita Falls → Abilene",      (-98.49, 33.91), (-99.73, 32.45)), | ] |  | # your code here | # expected output: table sorted by error % descending`

- Cell 15
  - Prompt: ## Exercise B — Find the Crossover Point  Starting from the base point `(-98.49, 33.91)`, step east in 0.5° increments and compute both distances for each step. Find the approximate separation (in km) where the Euclidean error first exceeds **5%**.  Print the crossover row.
  - Source: `base = (-98.49, 33.91) |  | # your code here | # step east from base in 0.5° increments up to 20° | # for each step: compute euclidean_distance, haversine_km, pct_error | # stop and print the first row where error > 5%`


### Assignments\02-Missile_Geometry_202\_micro_lessons\06-Distance\03-Distance_Applications.ipynb

- Cell 16
  - Prompt: ---  ## Exercise A — Find the Nearest 5 Airfields  Given a new query point, find the 5 nearest airfields from the `airfields` list. Print each name and distance. Then display them on a map with lines from the query to each result.
  - Source: `query_b = (-100.0, 35.0)   # somewhere in the Texas panhandle |  | # your code here | # 1. use nearest_n to get the 5 closest airfields | # 2. print name + distance for each | # 3. display on a map with lines from query_b to each result`

- Cell 20
  - Prompt: ## Exercise C — Click-to-Range  Extend the click map from Section 2. When the user clicks, draw a 150 km range circle around the click point and highlight any airfields inside it with a different marker color. Print the count and names in the output widget.
  - Source: `# your code here | # hint: use circle_polygon() to build the ring, GeoJSON layer to display it, | # and within_radius() to find airfields inside it | # remove and re-add the circle layer on each click`


### Assignments\02-Missile_Geometry_202\_micro_lessons\06-Distance\04-Performance_Batching.ipynb

- Cell 17
  - Prompt: ---  ## Exercise A — Nearest City to Each Military Base  The `Military_Bases.geojson` file contains 824 US military bases as polygon features. Compute the centroid of each base's exterior ring, then use `haversine_vectorized` to find the nearest world city to each base. Print the 10 base–city pairs with the shortest distance.
  - Source: `with open(DATA_PATH / "Military_Bases.geojson") as f: |     bases_geojson = json.load(f) |  | def polygon_centroid(ring): |     """Compute the mean [lon, lat] of a coordinate ring.""" |     lons = [v[0] for v in ring] |     lats = [v[1] for v in ring] |     return sum(lons) / len(lons), sum(lats) / len(lats) |  | # Extract centroids from each base's first exterior ring | bases = [] | for feature in bases_geojson["features"]: |     geom = feature["geometry"] |     name = feature["properties"].get("featureName", "Unknown") |     # MultiPolygon: coordinates[polygon_idx][ring_idx][vertex_idx] |     exterior_ring = geom["coordinates"][0][0] |     clon, clat = polygon_centroid(exterior_ring) |     bases.append({"name": name, "lon": clon, "lat": clat}) |  | print(f"Loaded {len(bases)} base centroids") | print("Sample:", bases[0]) |  | # your code here: | # for each base, use haversine_vectorize`

- Cell 19
  - Prompt: ## Exercise B — Cities Within Range of Any Base  Using `within_radius_bbox`, find all world cities within **50 km** of at least one US military base. How many unique cities qualify? Print the top 10 cities that are closest to any base, along with which base they are nearest to.
  - Source: `# your code here | # hint: loop over bases, call within_radius_bbox(base_coord, all_cities, 50) | # collect results into a dict keyed by city name to avoid duplicates | # track which base produced the smallest distance for each city`

- Cell 21
  - Prompt: ## Exercise C — Time Your Own Query  Pick a launch point from the final project or any coordinate you find interesting. Run all four approaches against the full world cities dataset:  1. Explicit loop 2. List comprehension 3. Comprehension + bbox pre-filter 4. NumPy vectorized  Time each one and print a summary table. Find the top 5 nearest cities using the NumPy result.
  - Source: `my_query = (-98.49, 33.91)   # replace with your own point |  | # your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\07-Bearing\00-What_Is_Bearing.ipynb

- Cell 15
  - Prompt: ## Exercise B — Normalize Invalid Values  Bearing must always be in `[0, 360)`. Each value below is the output of a raw `atan2` calculation that forgot to normalize. Write code to fix each one using `(value + 360) % 360`.  ```python raw_bearings = [-45, -90, -180, 380, 400, -1, 720] ```  Print each raw value alongside its normalized result.
  - Source: `raw_bearings = [-45, -90, -180, 380, 400, -1, 720] |  | # your code here | # hint: (value + 360) % 360 handles negative values, | #       but won't fix values > 360 on its own — think about why`


### Assignments\02-Missile_Geometry_202\_micro_lessons\07-Bearing\01-Compute_Bearing.ipynb

- Cell 14
  - Prompt: Each line radiates out from Wichita Falls. The bearing labels in the `properties` field confirm the direction. You can cross-reference with the compass rose from the previous notebook: a line pointing northeast should carry a bearing between 45° and 90°.  ---  ## Exercise A — Compute Bearings Between Cities  Using `compute_bearing`, compute the bearing for each route below. Print the result alongside the route label.  ```python routes = [     ("Tinker AFB → Fort Smith",   [-97.37, 35.39], [-94.37, 35.34]),     ("Tinker AFB → Lubbock",      [-97.37, 35.39], [-101.70, 33.66]),     ("NAS Fort Worth → Kelly",    [-97.04, 32.85], [-98.47, 29.53]),     ("Kelly → Tinker AFB",        [-98.47, 29.53], [-97.37, 35.39]), ] ```  For each result, also write (as a comment) whether the bearing is in the North, East, South, or West half of the compass.
  - Source: `routes = [ |     ("Tinker AFB → Fort Smith",   [-97.37, 35.39], [-94.37, 35.34]), |     ("Tinker AFB → Lubbock",      [-97.37, 35.39], [-101.70, 33.66]), |     ("NAS Fort Worth → Kelly",    [-97.04, 32.85], [-98.47, 29.53]), |     ("Kelly → Tinker AFB",        [-98.47, 29.53], [-97.37, 35.39]), | ] |  | # your code here`

- Cell 16
  - Prompt: ## Exercise B — Reverse Bearing  The bearing from A → B and the bearing from B → A are **not** simply `180°` apart on a sphere (though they are close for short distances).  1. Compute `compute_bearing(p1, p2)` for any two cities from Exercise A. 2. Then compute `compute_bearing(p2, p1)` (the reverse direction). 3. Compute the difference between the two results. 4. Is the difference exactly `180°`? Why or why not?
  - Source: `# your code here | # pick any pair from Exercise A and compute both directions`

- Cell 18
  - Prompt: ## Exercise C — Edge Cases  Test `compute_bearing` with the following edge-case inputs. For each, predict the result *before* running the code, then verify.  ```python # Same point — p1 == p2 same = [-98.49, 33.91]  # Exactly due north on the same meridian wf_north = ([-98.49, 33.91], [-98.49, 40.00])  # Cross the prime meridian — from just west to just east cross_pm = ([-0.5, 51.5], [0.5, 51.5])  # Cross the antimeridian — from just east of 180° to just west # (use 179.9 → -179.9, both at lat 0) cross_anti = ([179.9, 0.0], [-179.9, 0.0]) ```  Which cases produce expected results? Which (if any) might surprise you?
  - Source: `same      = [-98.49, 33.91] | wf_north  = ([-98.49, 33.91], [-98.49, 40.00]) | cross_pm  = ([-0.5, 51.5],   [ 0.5, 51.5]) | cross_anti = ([179.9, 0.0],  [-179.9, 0.0]) |  | # your code here — run each and note whether the result matches your prediction`


### Assignments\02-Missile_Geometry_202\_micro_lessons\07-Bearing\02-Bearing_V_Direction.ipynb

- Cell 12
  - Prompt: The drift is negligible for nearby targets and grows with distance. At intercontinental ranges the heading has rotated by several degrees before you are even halfway there.  ---  ## Exercise A — Drift by Direction  Bearing drift is not equal in all directions. A due-east path at mid-latitudes drifts differently than a northeast path.  Using Wichita Falls as the base point, compute initial vs. midpoint bearing for each of the four routes below. Which direction shows the most drift? Which shows the least?  ```python routes = [     ("Due East (~900 km)",       [-87.0,  33.91]),     ("Due North (~900 km)",      [-98.49, 41.99]),     ("Northeast (~900 km)",      [-91.0,  40.0 ]),     ("Southeast (~900 km)",      [-91.0,  27.0 ]), ] ```
  - Source: `base = [-98.49, 33.91] |  | routes = [ |     ("Due East (~900 km)",   [-87.0,  33.91]), |     ("Due North (~900 km)",  [-98.49, 41.99]), |     ("Northeast (~900 km)",  [-91.0,  40.0 ]), |     ("Southeast (~900 km)",  [-91.0,  27.0 ]), | ] |  | # your code here`

- Cell 16
  - Prompt: ## Exercise C — Map the Bearing Drift  Using the Dallas → London route, draw a map (ipyleaflet) with: - The path as a LineString - A marker at each of the 8 intermediate points - Each marker labeled with its local bearing at that step  Use `fit_bounds` to frame the map to the route extent.
  - Source: `from ipyleaflet import Map, GeoJSON |  | # your code here | # hint: build path_points using bearing_along_path's intermediate coords | # hint: fit_bounds expects [[south, west], [north, east]]`


### Assignments\02-Missile_Geometry_202\_micro_lessons\07-Bearing\03-Bearing_Applications.ipynb

- Cell 12
  - Prompt: Green targets are in range. Gray targets are not. The dashed lines from the launch site show the exact bearing to each reachable target. Adjust `MAX_RANGE_KM` and rerun to see the picture change.  ---  ## Exercise A — Interactive Range Slider  Wire the targeting picture to an `ipywidgets.IntSlider` so that changing the range updates which targets are highlighted and which lines are drawn, without rewriting the map from scratch.
  - Source: `import ipywidgets as widgets | from ipyleaflet import Map, GeoJSON |  | # your code here | # hint: build the map once, then use observe() on the slider value | # hint: remove old GeoJSON layers before adding updated ones | # use m.layers to track what's been added |  | slider = widgets.IntSlider(value=300, min=50, max=800, step=50, |                            description="Range (km):") | out = widgets.Output() |  | # your update function and map display here`

- Cell 14
  - Prompt: ## Exercise B — Sector + Range Combined  Write a function `targets_in_envelope(origin, features, start_bearing, end_bearing, max_range_km)` that returns only targets that satisfy **both** constraints: within the bearing sector **and** within the range.  Test it with a northeast sector (0°–90°) at 500 km from Wichita Falls. Print the name, bearing, and distance of each result.
  - Source: `def targets_in_envelope(origin, features, start_bearing, end_bearing, max_range_km): |     # your code here |     pass |  | results = targets_in_envelope(launch, features, 0, 90, 500) | for feat, brg, dist in (results or []): |     print(f"  {feat['properties']['name']:<26}  {brg:.1f}°  {dist:.0f} km")`

- Cell 16
  - Prompt: ## Exercise C — Nearest Target by Direction  Given a desired heading of `45°` (northeast), find the target whose actual bearing from the launch site is **closest to that heading**, regardless of distance.  Write a function `nearest_by_bearing(origin, features, desired_bearing)` that returns the single closest-bearing target. Account for wraparound so that a target at `359°` is considered close to a desired bearing of `1°`.
  - Source: `def bearing_diff(a, b): |     """Shortest angular difference between two bearings, in [0, 180].""" |     diff = abs(a - b) % 360 |     return min(diff, 360 - diff) |  | def nearest_by_bearing(origin, features, desired_bearing): |     # your code here |     pass |  | result = nearest_by_bearing(launch, features, 45) | if result: |     feat, brg = result |     print(f"Nearest to 45°: {feat['properties']['name']}  ({brg:.1f}°)")`


### Assignments\02-Missile_Geometry_202\_micro_lessons\07-Bearing\04-Advanced_Bearing.ipynb

- Cell 13
  - Prompt: The required bearing shifts continuously as the target moves east. At hour 0 the target is northwest; by hour 4 it has moved far enough east that the required bearing is also shifting eastward. This is bearing-over-time — the foundation of lead-angle and intercept calculation.  ---  ## Exercise A — Multi-Leg Route  A route makes three stops: Wichita Falls → Chicago → New York → London.  For each leg, compute and print: - initial bearing - final bearing   - distance - the delta between initial and final bearing  Then compute the **total route distance** and identify which leg has the largest bearing drift.
  - Source: `waypoints = [ |     ("Wichita Falls", [-98.49, 33.91]), |     ("Chicago",       [-87.63, 41.88]), |     ("New York",      [-74.01, 40.71]), |     ("London",        [ -0.13, 51.51]), | ] |  | # your code here`

- Cell 15
  - Prompt: ## Exercise B — Great-Circle Path on a Map  Using `great_circle_path`, draw the arcs for all three legs of the route above on a single ipyleaflet map. Use a different color per leg. Add markers at each waypoint.
  - Source: `leg_colors = ["#e63946", "#457b9d", "#2a9d8f"] |  | # your code here | # hint: zip(waypoints[:-1], waypoints[1:]) to iterate leg pairs`

- Cell 17
  - Prompt: ## Exercise C — Intercept Bearing  A target is moving due north at 300 km/h, starting from `[-97.0, 30.0]`. Your launch site is at `[-98.49, 33.91]` (Wichita Falls). Your projectile travels at 600 km/h.  Find the intercept: the target position and required bearing such that your projectile, fired now, arrives at the same point at the same time as the target.  Approach: 1. For each time step `t` (in hours, try 0.1 to 3.0 in steps of 0.1), compute where the target will be 2. Compute the distance from your launch site to that future position 3. Compute the time your projectile would take to cover that distance at 600 km/h 4. Find the `t` where projectile travel time ≈ `t` (they meet) 5. Report the intercept point and the bearing to fire
  - Source: `target_start   = [-97.0, 30.0] | target_heading = 0      # due north | target_speed   = 300    # km/h | projectile_speed = 600  # km/h | launch = [-98.49, 33.91] |  | # your code here | # hint: find t where haversine_km(launch, target_at_t) / projectile_speed ≈ t`


### Assignments\02-Missile_Geometry_202\_micro_lessons\08-Intercept_Pursuit_Module_Design\00-Problem_Setup.ipynb

- Cell 13
  - Prompt: ## Exercise B — Map the Correct Question  For each time step `t` from 0.1 to 1.5 hours (in steps of 0.1), compute: - Where the target will be at time `t` - The distance from the shooter to that future position - The distance the interceptor can travel in time `t` (`shooter_speed × t`)  Plot both distances on a single matplotlib chart against time. The intercept time is where the two lines cross.
  - Source: `import matplotlib.pyplot as plt |  | times = [t / 10 for t in range(1, 16)]  # 0.1 to 1.5 hours |  | # your code here | # for each t: | #   target_future = destination_point(target_pos, target_heading, target_speed * t) | #   dist_to_future = haversine_km(shooter_pos, target_future) | #   interceptor_reach = shooter_speed * t | # plot both against time, mark the crossing`


### Assignments\02-Missile_Geometry_202\_micro_lessons\08-Intercept_Pursuit_Module_Design\01-Constant_Velocity_Intercept.ipynb

- Cell 16
  - Prompt: ## Exercise C — Multiple Incoming Targets  Given the three targets below, each with different positions, speeds, and headings, compute the intercept solution for each. Print a ranked table sorted by time of flight (soonest threat first).  ```python targets = [     {"pos": [-103.0, 37.0], "heading": 135, "speed": 250},     {"pos": [-96.0,  38.0], "heading": 210, "speed": 400},     {"pos": [-100.5, 35.0], "heading":  90, "speed": 180}, ] shooter_speed = 600 ```
  - Source: `targets = [ |     {"pos": [-103.0, 37.0], "heading": 135, "speed": 250}, |     {"pos": [-96.0,  38.0], "heading": 210, "speed": 400}, |     {"pos": [-100.5, 35.0], "heading":  90, "speed": 180}, | ] |  | # your code here — compute intercept for each, sort by TOF, print ranked table`


### Assignments\02-Missile_Geometry_202\_micro_lessons\08-Intercept_Pursuit_Module_Design\02-Iterative_Pursuit.ipynb

- Cell 13
  - Prompt: ## Exercise B — Map Multiple Pursuit Curves  Run `simulate_pursuit` for four different target headings (`45°`, `135°`, `225°`, `315°`) against the same shooter. Plot all four pursuit paths on a single ipyleaflet map using a different color per heading. Add the target start position and the shooter position as markers.  Which curves are shortest? Which are longest? Does the shape of the curve tell you anything about the geometry?
  - Source: `headings_to_plot = [45, 135, 225, 315] | colors = ["#e63946", "#2a9d8f", "#e9c46a", "#457b9d"] |  | # your code here | # hint: subsample each path (every Nth point) before adding to the map`

- Cell 15
  - Prompt: ## Exercise C — Pursuit vs. Intercept Time Budget  For the baseline scenario, the intercept solution takes less time than pure pursuit. How much less depends on target heading.   For each heading in `range(0, 360, 15)`: 1. Run `simulate_pursuit` and record the pursuit time (or `None` if it fails) 2. Run `find_intercept_time` and record the intercept time (or `None`) 3. Compute the time saved by using intercept over pursuit  Print a table and identify: which heading maximizes the time savings? Which heading makes pursuit and intercept nearly equivalent?
  - Source: `# your code here | # hint: use shooter_speed=600, target_speed=300 for both methods`


### Assignments\02-Missile_Geometry_202\_micro_lessons\08-Intercept_Pursuit_Module_Design\04-Strategy_and_Limits.ipynb

- Cell 16
  - Prompt: ---  ## Exercise A — Escape Cone by Speed Ratio  Compute and plot the escape cone half-angle as the speed ratio `s_spd / t_spd` varies from 0.3 to 1.5, holding target speed at 400 km/h.  Use `escape_cone_half_angle`. For speed ratios ≥ 1.0, plot 0° (no escape cone). For ratios < 1.0, plot the actual half-angle.  Your plot: speed ratio on x-axis, escape cone half-angle (degrees) on y-axis.  Then answer: at what speed ratio does the escape cone cover more than half the hemisphere (i.e., half-angle > 90°)?
  - Source: `# Exercise A — your code here |  | t_spd = 400 | ratios = [r / 100 for r in range(30, 155, 5)]   # 0.30 to 1.50 |  | angles = [] | for ratio in ratios: |     s_spd = t_spd * ratio |     a = escape_cone_half_angle(s_spd, t_spd) |     angles.append(a if a is not None else 0.0) |  | fig, ax = plt.subplots(figsize=(9, 4)) | ax.plot(ratios, angles, "o-", color="#e63946", markersize=4) | ax.axhline(90, color="#888", linestyle="--", linewidth=1, label="90° threshold") | ax.axvline(1.0, color="#aaa", linestyle=":", linewidth=1, label="Equal speeds") | ax.fill_between(ratios, angles, 0, alpha=0.15, color="#e63946") | ax.set_xlabel("Speed ratio  (shooter / target)") | ax.set_ylabel("Escape cone half-angle (°)") | ax.set_title("Escape cone grows as target outpaces shooter") | ax.legend() | ax.grid(True, alpha=0.3) | plt.tight_layout() | plt.show()`

- Cell 18
  - Prompt: ## Exercise B — Delay Budget vs. Speed Ratio  For the same scenario (WF shooter, NW target, SE heading 135°), sweep shooter speed from 350 to 800 km/h and compute the **maximum acceptable delay** at each speed using `max_delay`.  Plot shooter speed on the x-axis and maximum acceptable delay (minutes) on the y-axis. Annotate the point where the delay budget first exceeds 10 minutes.  Then answer: a commander needs a minimum 8-minute decision window. What is the minimum shooter speed required for this scenario?
  - Source: `# Exercise B — your code here |  | s_pos  = [-98.49, 33.91] | t_pos  = [-101.0, 36.5] | t_hdg  = 135 | t_spd  = 300 |  | speeds = list(range(350, 825, 25)) | delays = [] | for s_spd in speeds: |     delays.append(max_delay(s_pos, t_pos, t_hdg, t_spd, s_spd)) |  | fig, ax = plt.subplots(figsize=(9, 4)) | valid_s = [s for s, d in zip(speeds, delays) if d is not None] | valid_d = [d for d in delays if d is not None] |  | ax.plot(valid_s, valid_d, "o-", color="#2a9d8f", markersize=5) | ax.axhline(10, color="#e63946", linestyle="--", linewidth=1, label="10-min threshold") | ax.axhline(8,  color="#f4a261", linestyle="--", linewidth=1, label="8-min requirement") | ax.set_xlabel("Shooter speed (km/h)") | ax.set_ylabel("Max acceptable delay (min)") | ax.set_title("Reaction time budget vs. shooter speed  (target 300 km/h, hdg 135°)") | ax.legend() | ax.grid(True, alpha=0.3) | plt.tight_layout() | `

- Cell 20
  - Prompt: ## Exercise C — Optimal Shooter Position  The target starts at `[-101.0, 36.5]` heading SE at 135°, 300 km/h. The shooter moves at 700 km/h.  You have a choice of where to pre-position the shooter — anywhere within 300 km of the target's starting point. Your objective: **maximize the delay budget** (i.e., find the shooter position that allows the longest reaction time before the shot must be fired).  Sample 360 positions around the target at 200 km radius. For each, compute `max_delay`. Find and print the best position, then put all 360 positions on a map colored by delay budget.
  - Source: `# Exercise C — your code here |  | t_pos = [-101.0, 36.5] | t_hdg = 135 | t_spd = 300 | s_spd = 700 | radius_km = 200 |  | ring_bearings = list(range(0, 360, 5))   # 72 positions | ring_positions = [destination_point(t_pos, b, radius_km) for b in ring_bearings] | ring_delays    = [max_delay(sp, t_pos, t_hdg, t_spd, s_spd) for sp in ring_positions] |  | valid_pairs = [(b, sp, d) for b, sp, d in zip(ring_bearings, ring_positions, ring_delays) |                if d is not None] | if valid_pairs: |     best = max(valid_pairs, key=lambda x: x[2]) |     print(f"Best position: bearing {best[0]}° from target  →  {best[1]}  →  delay = {best[2]:.1f} min") |  | # Map | ring_map = Map(center=(35.5, -100.0), zoom=6) |  | max_d = max((d for d in ring_delays if d is not None), default=1) | for sp, md in zip(ring_positions, ring_delays): |     if md is None: |         color = "#aaa" |     else: |       `


### Assignments\02-Missile_Geometry_202\_micro_lessons\08-Intercept_Pursuit_Module_Design\05-Advanced_Topics.ipynb

- Cell 17
  - Prompt: ## Exercise C — Build a Defense System  Using the multi-threat prioritization code from Section 3, build a simple automated defense system.  **Rules:** - You have one shooter that can engage one target at a time - After each engagement (intercept computed), assume the shot is "in the air" for its TOF before the next engagement begins - Prioritize by **earliest time to impact** (TTI) - If a threat has no TTI (will miss the asset), skip it  Write a function `engagement_sequence(threats, shooter_pos, shooter_speed, defended_point)` that: 1. Ranks threats by TTI 2. Fires at each in order, tracking accumulated time 3. Prints the engagement order with fire time, TOF, and whether each threat was intercepted before it reached the asset  Test it on the 4-threat scenario from Section 3 plus one additional threat of your choice.
  - Source: `# Exercise C — your code here |  | def engagement_sequence(threats, shooter_pos, shooter_speed, defended_point): |     """ |     Simple sequential engagement planner. |     Prioritizes by TTI; skips threats that won't reach the asset. |     """ |     # Compute TTI and intercept TOF for all threats |     annotated = [] |     for thr in threats: |         tti = time_to_impact(thr["pos"], thr["hdg"], thr["spd"], defended_point) |         tof = find_intercept_time(shooter_pos, thr["pos"], thr["hdg"], |                                   thr["spd"], shooter_speed, t_max=15.0) |         if tti is not None: |             annotated.append({**thr, "tti_h": tti, "tof_h": tof}) |  |     # Sort by TTI |     annotated.sort(key=lambda x: x["tti_h"]) |  |     print(f"{'#':<3}  {'ID':<5}  {'Fire at (min)':>13}  {'TOF (min)':>10}  " |           f"{'Impact at (min)':>16}  {'Intercepted?':>13}") |     print`


### Assignments\02-Missile_Geometry_202\_micro_lessons\09-Intersections\00-Lines_as_Paths.ipynb

- Cell 15
  - Prompt: ## Exercise A  A direct flight from **Los Angeles** (`[-118.243, 34.052]`) to **London** (`[-0.127, 51.507]`) is routed through a waypoint over **Reykjavik, Iceland** (`[-22.000, 64.133]`).  1. Build a `LineString` Feature with all three points and a `"name"` property of `"LA to London"`. 2. Wrap it in a `FeatureCollection` and display it on a world map centered at `(50, -50)`, zoom 3. 3. Print the number of segments.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # 1. Build the LineString Feature (3 points, 2 segments) | # 2. Wrap in FeatureCollection and display on a world map | # 3. Print number of segments | # Your code here`

- Cell 17
  - Prompt: ## Exercise B  You are given a list of `(lat, lon)` tuples — note the **lat/lon order**, which is the opposite of GeoJSON's `[lon, lat]`.  ```python waypoints_latlon = [     (48.857,   2.352),   # Paris     (41.890,  12.492),   # Rome     (37.983,  23.727),   # Athens     (41.015,  28.979),   # Istanbul     (30.044,  31.236),   # Cairo ] ```  1. Convert the list to GeoJSON `[lon, lat]` coordinate order. 2. Build a `LineString` Feature with `"name": "Mediterranean Arc"`. 3. Save it as `data/med_arc.geojson`. 4. Load the file back and print the coordinate count to confirm the round-trip.
  - Source: `import json | from pathlib import Path |  | waypoints_latlon = [ |     (48.857,   2.352),   # Paris |     (41.890,  12.492),   # Rome |     (37.983,  23.727),   # Athens |     (41.015,  28.979),   # Istanbul |     (30.044,  31.236),   # Cairo | ] |  | # 1. Convert to [lon, lat] order | # 2. Build the Feature | # 3. Save to data/med_arc.geojson | # 4. Load back and confirm coordinate count | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\09-Intersections\01-Line_Segment_Intersection.ipynb

- Cell 15
  - Prompt: ## Exercise A  Inspect the four segment pairs below **by eye** first — predict whether each pair intersects or not, then run `segments_intersect` to check your prediction.  ```python pairs = [     # pair 1     ([0, 0], [4, 4],  [0, 4], [4, 0]),     # pair 2     ([0, 0], [2, 0],  [3, 0], [5, 0]),     # pair 3     ([0, 0], [3, 0],  [2, 0], [2, 3]),     # pair 4     ([0, 2], [4, 2],  [5, 0], [5, 4]), ] ```  Print your prediction and the function result side by side for each pair.
  - Source: `pairs = [ |     ([0, 0], [4, 4],  [0, 4], [4, 0]),   # pair 1 |     ([0, 0], [2, 0],  [3, 0], [5, 0]),   # pair 2 |     ([0, 0], [3, 0],  [2, 0], [2, 3]),   # pair 3 |     ([0, 2], [4, 2],  [5, 0], [5, 4]),   # pair 4 | ] |  | # For each pair, write your prediction as True/False, then call segments_intersect | my_predictions = [True, False, True, False]   # replace with your guesses |  | # Your code here: compare predictions to segments_intersect results`

- Cell 17
  - Prompt: ## Exercise B  Implement `segments_intersect` yourself using `orientation` and `on_segment` as building blocks. Both helpers are provided — your job is the logic that combines them.  Verify your implementation against the four test cases at the bottom of the cell.
  - Source: `def orientation(p, q, r): |     return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0]) |  | def on_segment(p, q, r): |     return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and |             min(p[1], r[1]) <= q[1] <= max(p[1], r[1])) |  | def segments_intersect(p1, p2, p3, p4): |     """ |     Returns True if segment p1-p2 intersects segment p3-p4. |     Hint: compute 4 orientation values, check general case first, |     then handle collinear edge cases with on_segment. |     """ |     # Your code here |     pass |  |  | # Verification — all four should pass | assert segments_intersect([0,0],[4,4],[0,4],[4,0]) == True,  "X-cross should intersect" | assert segments_intersect([0,0],[2,0],[3,0],[5,0]) == False, "Collinear gap should not intersect" | assert segments_intersect([0,0],[3,0],[2,0],[2,3]) == True,  "T-junction should intersect" | assert segments_intersect([0,2],[4`


### Assignments\02-Missile_Geometry_202\_micro_lessons\09-Intersections\02-Line_vs_Polygon_Basics.ipynb

- Cell 13
  - Prompt: ## Exercise A  The polygon below is a rough bounding outline of Iraq.  ```python iraq_rough = {     "type": "Polygon",     "coordinates": [[         [38.8, 37.4], [48.8, 37.4], [48.8, 29.1],         [44.7, 29.1], [38.8, 33.0], [38.8, 37.4]     ]] } ```  1. Use `polygon_edges` to extract and print all edges. 2. Count the edges and confirm it equals the number of ring positions minus one. 3. Visualize the polygon on a map centered over the Middle East.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | iraq_rough = { |     "type": "Polygon", |     "coordinates": [[ |         [38.8, 37.4], [48.8, 37.4], [48.8, 29.1], |         [44.7, 29.1], [38.8, 33.0], [38.8, 37.4] |     ]] | } |  | # 1. Extract and print all edges | # 2. Count edges vs ring positions | # 3. Display on a map | # Your code here`

- Cell 15
  - Prompt: ## Exercise B  The **Alpha** path from `paths.geojson` runs from Washington D.C. to Tehran. Test it against `iraq_rough` from Exercise A.  1. Extract the Alpha path segment (start and end coordinates). 2. Call `line_crosses_polygon` and print the result. 3. Call `line_crosses_polygon_fast` and confirm it returns the same result. 4. Display both the path and the polygon on the same map to visually verify.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # 1. Get Alpha path start/end coordinates from module_paths | # 2. Test with line_crosses_polygon | # 3. Test with line_crosses_polygon_fast and compare | # 4. Display both on a map | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\09-Intersections\03-Detecting_Intersections.ipynb

- Cell 11
  - Prompt: ## Exercise A  The **Delta** path runs from Moscow (`[37.617, 55.755]`) to Riyadh (`[46.675, 24.688]`).  1. Use `find_crossed_countries` to get the list of crossed countries. 2. Print their names in alphabetical order. 3. Print how many were skipped by the bbox pre-check vs how many required a full edge test.  For part 3, modify `path_crosses_feature` to count skips and full-tests, or add print statements temporarily.
  - Source: `# Get the Delta path from module_paths | # 1. Find crossed countries | # 2. Print names alphabetically | # 3. Count bbox skips vs full edge tests | # Your code here`

- Cell 13
  - Prompt: ## Exercise B  Write a function `crossed_country_names(path_feature, countries_fc)` that returns a **sorted list of country name strings** (not Feature objects) for the countries a path crosses.  Then use it to answer: **which path in the dataset crosses the most countries?**
  - Source: `def crossed_country_names(path_feature, countries_fc): |     """Return a sorted list of country name strings the path crosses.""" |     # Your code here |     pass |  |  | # Use it to find which path crosses the most countries | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\09-Intersections\04-Highlighting_Intersected_Features.ipynb

- Cell 10
  - Prompt: ## Exercise A  The **Charlie** path runs from Caracas, Venezuela to Madrid, Spain.  1. Find the countries Charlie crosses. 2. Build a two-layer map: crossed countries in **red** (`#e74c3c`), others in **gray** (`#bdc3c7`), with the Charlie path drawn in red. 3. Print the count and names of crossed countries.
  - Source: `# Get the Charlie path from module_paths | # 1. Find crossed countries | # 2. Build a two-layer map | # 3. Print count and names | # Your code here`

- Cell 12
  - Prompt: ## Exercise B  Build a **per-path layer map** using `LayersControl` so each path and its corresponding hit countries are a named, toggleable pair.  Use a different highlight color for each path:  | Path | Color | |---|---| | Alpha | `#e74c3c` | | Bravo | `#2980b9` | | Charlie | `#27ae60` | | Delta | `#8e44ad` |  Add a single dimmed base layer for all non-hit countries.
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | PATH_COLORS = { |     "Alpha":   "#e74c3c", |     "Bravo":   "#2980b9", |     "Charlie": "#27ae60", |     "Delta":   "#8e44ad", | } |  | # Build a LayersControl map with one hit-layer and one path-layer per route | # Plus a single dimmed base layer for all non-hit countries | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\09-Intersections\05-Applications_Missile_Paths.ipynb

- Cell 10
  - Prompt: ## Exercise A  Add a new path to the module dataset: a launch from **Beijing** (`[116.407, 39.904]`) to **Berlin** (`[13.405, 52.520]`) named `"Echo"`.  1. Build the Feature dict and append it to `module_paths["features"]`. 2. Call `path_report` on it and print the full result. 3. Display it with `path_map` using color `"#8e44ad"`.
  - Source: `# 1. Build the Echo Feature and append to module_paths | # 2. Generate and print the path_report | # 3. Display with path_map | # Your code here`

- Cell 12
  - Prompt: ## Exercise B  Using all paths now in `module_paths` (including Echo from Exercise A):  1. Find the path with the **greatest range**. 2. Find the path that crosses the **most countries**. 3. Find any **country that appears in more than one path's airspace** — list those countries and which paths they appear in.
  - Source: `# Make sure reports includes Echo before running this |  | # 1. Path with greatest range | # 2. Path crossing the most countries | # 3. Countries appearing in multiple paths' airspace | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\00_Buffer_Concepts.ipynb

- Cell 11
  - Prompt: ## Exercise A  Using the concept circle code from the teaching cell, modify it to draw **two concentric circles** around Riyadh (`[46.675, 24.688]`):  - Inner ring: `degree_radius = 1.5`, 32 points, red - Outer ring: `degree_radius = 3.0`, 32 points, orange  Add both as separate `GeoJSON` layers on the same map.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # Draw two concentric degree-offset circles around Riyadh | # Inner (1.5°, 32 pts, red) and outer (3.0°, 32 pts, orange) | # Your code here`

- Cell 13
  - Prompt: ## Exercise B  Using the corridor sketch code, draw a corridor along the path from **Tehran** (`[51.388, 35.695]`) to **Moscow** (`[37.617, 55.755]`) with a `degree_radius` of `1.5` and `30` sample points.  Display the corridor and the path line on the same map. Use a different color for the path vs the corridor.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # Draw a corridor along Tehran → Moscow | # degree_radius=1.5, 30 sample points, 16-pt circles | # Display corridor + path line with different colors | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\01_Buffering_Points.ipynb

- Cell 14
  - Prompt: ## Exercise A  Create a 200 km buffer around **Honolulu** (`[-157.855, 21.305]`) and display it on a world map.  1. Call `buffer_feature` with `radius_km=200` and `name="Honolulu 200 km"`. 2. Add the point itself as a separate Feature. 3. Display both on a map centered on Honolulu at zoom 5.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # 1. 200 km buffer around Honolulu | # 2. Point feature for Honolulu | # 3. Display on map centered at Honolulu, zoom 5 | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Create **three concentric buffers** (100 km, 250 km, 500 km) around **Madrid** (`[-3.703, 40.417]`) and display them in three different colors on a single map.  Print the number of vertices in each buffer's ring to confirm they are all using the default `n_points=64`.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | madrid = [-3.703, 40.417] |  | # Create 100, 250, 500 km buffers | # Display with different colors (large → small so inner rings are visible) | # Print vertex count for each | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\02-Buffering_Lines.ipynb

- Cell 13
  - Prompt: ## Exercise A  Buffer the **Delta** path (Moscow → Riyadh) with a `radius_km` of 150 km and `n_samples=40`.  1. Use `line_buffer` to create the corridor. 2. Display the corridor and the path line on the same map. 3. Print the number of circle polygons in the corridor.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # Get the Delta path | # 1. Create 150 km corridor with 40 samples | # 2. Display corridor + path | # 3. Print circle count | # Your code here`

- Cell 15
  - Prompt: ## Exercise B  Compare a **point buffer** and a **line buffer** for the same feature and radius.  1. Take the endpoint of the Alpha path (Tehran, `[51.388, 35.695]`). 2. Create a 200 km **point buffer** around Tehran. 3. Create a 200 km **line buffer** for the full Alpha path. 4. Display both on the same map. Describe the difference: which covers more area, and why?
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # 1-2. Point buffer around Tehran (200 km) | # 3.   Line buffer for Alpha path (200 km) | # 4.   Display both on same map, describe difference | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\03-Comparing_Buffer_Sizes.ipynb

- Cell 10
  - Prompt: ## Exercise A  Create **three concentric buffers** (75 km, 200 km, 450 km) around **Honolulu** (`[-157.855, 21.305]`).  1. Display all three on a single map with distinct colors. 2. Print the exclusive band area (km²) for each ring. 3. Which band has the largest area, and why?
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | honolulu = [-157.855, 21.305] |  | # 1. Three concentric buffers (75, 200, 450 km) | # 2. Print band areas | # 3. Identify and explain the largest band | # Your code here`

- Cell 12
  - Prompt: ## Exercise B  Create a 400 km buffer around **each** of the four targets (Tehran, Honolulu, Madrid, Riyadh) and display them all on a world map.  1. Use `LayersControl` so each target's buffer can be toggled. 2. Identify by inspection which pairs of buffers overlap. 3. Print the haversine distance between the two closest targets to confirm whether they should overlap.
  - Source: `import math | from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | def haversine_km(lon1, lat1, lon2, lat2): |     R = 6371.0 |     phi1, phi2 = math.radians(lat1), math.radians(lat2) |     dphi = math.radians(lat2 - lat1) |     dlam = math.radians(lon2 - lon1) |     a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlam/2)**2 |     return R * 2 * math.asin(math.sqrt(a)) |  | # 1. 400 km buffer around each target with LayersControl | # 2. Identify overlapping pairs by inspection | # 3. Print distances between all pairs, confirm which overlap at 400 km | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\04-Buffer_Visualization_Strategies.ipynb

- Cell 13
  - Prompt: ## Exercise A  Create a **four-zone impact map** around **Riyadh** with radii 30 km, 100 km, 250 km, and 500 km.  1. Assign a distinct color to each zone (your choice of palette — traffic light, cool-to-warm, or custom). 2. Set `fillOpacity` so that the outermost ring is the most transparent and the innermost is the most opaque. 3. Add a `LayersControl` so each zone can be toggled on/off. 4. Print the opacity values you chose and one sentence explaining your palette decision.
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | riyadh = target_coords("Riyadh") |  | # 1. Four zones: 30, 100, 250, 500 km with distinct colors | # 2. fillOpacity: outer most transparent → inner most opaque | # 3. LayersControl | # 4. Print opacity values + palette rationale | # Your code here`

- Cell 15
  - Prompt: ## Exercise B  Display **Tehran** and **Madrid** each with a 1200 km buffer on a world map.  1. Use border-only style (`fillOpacity ≤ 0.08`) with distinct colors per target. 2. Add a 300 km **concentric inner ring** for each target in the same color but with slightly higher opacity. 3. The result should show both targets, both ring sizes, and still allow you to read country names underneath. 4. Describe: do the 1200 km rings overlap? If so, what does that overlap represent geographically?
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | tehran = target_coords("Tehran") | madrid = target_coords("Madrid") |  | # 1. 1200 km border-only rings for Tehran + Madrid | # 2. 300 km inner rings, same color, slightly more opaque | # 3. Display together — underlying geography should be readable | # 4. Describe overlap | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\05-CRS_Limitations.ipynb

- Cell 12
  - Prompt: ## Exercise A  Compare degree-offset vs km-accurate 300 km buffers at **three latitudes**: 10°N, 35°N, and 65°N (all at the same longitude, e.g. 30°E).  1. Create a map showing all six buffers (two per latitude, different colors per method). 2. Print the E-W span in km for the degree buffer and the km buffer at each latitude. 3. At which latitude does the distortion first exceed 25%?
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | RADIUS_KM = 300 | LON = 30.0 | LATITUDES = [10, 35, 65] |  | # For each latitude: | #   - compute radius_deg = RADIUS_KM / 111 | #   - create degree_buffer (red) and km_buffer (blue) | #   - display all 6 on one map | # Print E-W span comparison and identify >25% distortion threshold | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  **Moscow** is at approximately `[37.617, 55.755]`.  1. Create a 600 km degree-offset buffer around Moscow. 2. Create a 600 km km-accurate buffer around Moscow. 3. Display both on the same map and describe the shape difference. 4. Calculate: if you used the degree buffer to decide whether a city is within 600 km, could you incorrectly *exclude* a city that is actually within range? Which direction would the error occur?
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | moscow = [37.617, 55.755] |  | # 1. 600 km degree buffer around Moscow | # 2. 600 km km buffer around Moscow | # 3. Display both — observe shape | # 4. Explain directional error (east-west vs north-south) | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\10-Buffers\06-Applications_Impact_Zones.ipynb

- Cell 12
  - Prompt: ## Exercise A  Build a **blast radius map for Riyadh** with three zones: 75 km (lethal), 200 km (damaging), 400 km (warning).  1. Display all three zones with appropriate colors and opacities. 2. Using a containment check (`haversine_km`), determine which of the other three targets (Tehran, Honolulu, Madrid) fall within Riyadh's 400 km warning zone. 3. Print the distance from Riyadh to each of the other targets and label each as inside or outside the zone.
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | riyadh = target_coords("Riyadh") |  | # 1. Three blast zones around Riyadh (75, 200, 400 km) | # 2. Containment check: which targets are within 400 km of Riyadh? | # 3. Print distances and inside/outside labels | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  Create a **complete trajectory analysis** for the **Delta path** (Moscow → Riyadh).  1. Draw a 100 km flight corridor along the Delta path. 2. Add blast zones (50 km, 150 km, 300 km) at the **destination** (Riyadh). 3. Add a 300 km blast zone at the **origin** (Moscow) to show the launch vicinity. 4. Display all layers on one map with a `LayersControl`. 5. Print the total path length (haversine from start to end) in km.
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps |  | delta = next(f for f in paths_fc["features"] if f["properties"]["name"] == "Delta") | moscow = delta["geometry"]["coordinates"][0] | riyadh = target_coords("Riyadh") |  | # 1. 100 km corridor along Delta | # 2. 50/150/300 km blast zones at Riyadh (destination) | # 3. 300 km blast zone at Moscow (origin) | # 4. Display all with LayersControl | # 5. Print path length in km | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\00_Click_Capture.ipynb

- Cell 15
  - Prompt: ## Exercise A  Create a map that **prints the click coordinates** in a clean format:  ``` Click #1:  lat=35.6950  lon=51.3880 Click #2:  lat=24.6880  lon=46.6750 Click #3:  lat=40.4170  lon=-3.7030 ```  1. Each click appends a new line (do **not** clear previous output). 2. Include a click counter (`#1`, `#2`, ...) in each line. 3. Click at least 3 different locations to verify it works.
  - Source: `from ipyleaflet import Map, basemaps | from ipywidgets import Output |  | # Counter and log | # Map with on_interaction handler | # Print formatted output, appending (not clearing) each click | # Your code here`

- Cell 17
  - Prompt: ## Exercise B  Store the **last clicked location** and print it on demand.  1. Create a map with a click handler that stores the most recent click. 2. After clicking the map, run a separate cell that reads and prints the stored value. 3. Add a guard: if no click has been recorded yet, print `"No click yet"` instead of crashing.
  - Source: `from ipyleaflet import Map, basemaps | from ipywidgets import Output |  | # Map + click handler (stores last click) | # Your code here`

- Cell 18
  - Prompt: ## Exercise B  Store the **last clicked location** and print it on demand.  1. Create a map with a click handler that stores the most recent click. 2. After clicking the map, run a separate cell that reads and prints the stored value. 3. Add a guard: if no click has been recorded yet, print `"No click yet"` instead of crashing.
  - Source: `# Run this cell after clicking the map above | # Print stored click or "No click yet" | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\01_Point_Representation.ipynb

- Cell 13
  - Prompt: ## Exercise A  Write a function `format_point(click_coords)` that takes ipyleaflet click coordinates and returns a GeoJSON Point Feature.  1. The function must include a `"click_index"` property that you pass in as a second argument. 2. Test it with these manually-specified fake click coordinates:    - `[35.695, 51.388]` → Tehran    - `[24.688, 46.675]` → Riyadh    - `[40.417, -3.703]` → Madrid 3. Print the GeoJSON coordinates for each and verify the lon/lat order is correct.
  - Source: `import json |  | def format_point(click_coords, click_index): |     # click_coords is [lat, lon] from ipyleaflet |     # return a GeoJSON Feature with coordinates [lon, lat] |     # include click_index in properties |     pass  # your code here |  | test_clicks = [ |     ([35.695, 51.388], "Tehran"), |     ([24.688, 46.675], "Riyadh"), |     ([40.417, -3.703], "Madrid"), | ] |  | for i, (coords, name) in enumerate(test_clicks): |     feat = format_point(coords, i + 1) |     # print the GeoJSON coords — should be [lon, lat] |     # Your code here`

- Cell 15
  - Prompt: ## Exercise B  Create a map that places a **Marker** at each click and simultaneously adds the click as a **GeoJSON Point** layer.  1. The Marker and the GeoJSON point must appear at the exact same location. 2. After 3 clicks, print the GeoJSON coordinates of all stored points. 3. Verify each point's `coordinates` field is in `[lon, lat]` order (longitude first).
  - Source: `from ipyleaflet import Map, GeoJSON, Marker, basemaps | from ipywidgets import Output |  | # Map + handler: place Marker AND GeoJSON point at each click | # After 3 clicks, print stored coordinates in [lon, lat] order | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\02_Point_In_Polygon_Basics.ipynb

- Cell 14
  - Prompt: ## Exercise A  Load `data/regions.geojson` and create a map showing all five sectors.  Given these test points, predict by visual inspection which sector (if any) each one falls in:  | Point | lon | lat | Predicted sector | |---|---|---|---| | Tehran | 51.388 | 35.695 | ? | | Riyadh | 46.675 | 24.688 | ? | | Cairo | 31.235 | 30.044 | ? | | Madrid | -3.703 | 40.417 | ? | | Muscat | 58.593 | 23.614 | ? |  Write your predictions as comments in the code. We'll verify them programmatically in notebook 03.
  - Source: `import json | from pathlib import Path | from ipyleaflet import Map, GeoJSON, basemaps |  | DATA_DIR = Path("data") |  | with open(DATA_DIR / "regions.geojson") as f: |     regions = json.load(f) |  | test_points = [ |     {"name": "Tehran",  "lon": 51.388, "lat": 35.695, "predicted": "???"},  # your prediction |     {"name": "Riyadh",  "lon": 46.675, "lat": 24.688, "predicted": "???"}, |     {"name": "Cairo",   "lon": 31.235, "lat": 30.044, "predicted": "???"}, |     {"name": "Madrid",  "lon": -3.703, "lat": 40.417, "predicted": "???"}, |     {"name": "Muscat",  "lon": 58.593, "lat": 23.614, "predicted": "???"}, | ] |  | # Display all sectors + test points on a map | # Print your predictions as comments | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Define a **non-rectangular polygon** of your own — at least 6 vertices, with at least one concave angle (a notch or indentation).  1. Make sure the ring is properly closed (first point == last point). 2. Display it on a map. 3. Place one point that is inside the bounding box but outside the polygon (in the notch). 4. Place one point that is clearly inside the polygon. 5. Print both points' coordinates and mark which is inside and which is outside by visual inspection.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps |  | # Define a non-rectangular polygon (at least 6 vertices, at least one concave angle) | # Ensure ring is closed | # Place one point in the notch (inside bbox, outside polygon) | # Place one point clearly inside | # Display on map and print coordinates | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\03_Ray_Casting_Algorithm.ipynb

- Cell 13
  - Prompt: ## Exercise A  Implement `point_in_ring` yourself from scratch — without looking at the teaching cell above.  1. Start from the pseudocode: loop over edges, check if the ray at `lat` is straddled, compute the x-intersection, toggle `inside`. 2. Verify your implementation passes all five assertions below.
  - Source: `def my_point_in_ring(lon, lat, ring): |     # Your implementation here |     pass |  | alpha_ring = regions_fc["features"][0]["geometry"]["coordinates"][0] |  | assert my_point_in_ring(51.388, 35.695, alpha_ring) == True,  "Tehran should be inside Sector Alpha" | assert my_point_in_ring(50.0,   38.0,   alpha_ring) == True,  "Center should be inside" | assert my_point_in_ring(30.0,   38.0,   alpha_ring) == False, "West should be outside" | assert my_point_in_ring(70.0,   38.0,   alpha_ring) == False, "East should be outside" | assert my_point_in_ring(50.0,   20.0,   alpha_ring) == False, "South should be outside" |  | print("All assertions passed!")`

- Cell 15
  - Prompt: ## Exercise B  Use `point_in_ring` to verify your predictions from Exercise A of notebook 02.  For each test city, run the algorithm against the correct sector's ring and print whether it's inside or outside. Were your visual predictions accurate?
  - Source: `import json | from pathlib import Path |  | DATA_DIR = Path("data") | with open(DATA_DIR / "regions.geojson") as f: |     regions_fc = json.load(f) |  | cities = [ |     {"name": "Tehran",  "lon": 51.388, "lat": 35.695}, |     {"name": "Riyadh",  "lon": 46.675, "lat": 24.688}, |     {"name": "Cairo",   "lon": 31.235, "lat": 30.044}, |     {"name": "Madrid",  "lon": -3.703, "lat": 40.417}, |     {"name": "Muscat",  "lon": 58.593, "lat": 23.614}, | ] |  | # For each city, test against every sector | # Print: city name, sector name, inside=True/False | # Report which sector each city falls in (or "none") | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\04_Testing_Against_Multiple_Features.ipynb

- Cell 12
  - Prompt: ## Exercise A  Write a function `which_sector(lon, lat)` that takes a point and returns the name of the sector it falls in (or `"none"`).  1. Use `find_containing_feature` (early exit) internally. 2. Test it with Tehran, Riyadh, Cairo, Madrid, and Muscat. 3. Print a clean table: city name, lon, lat, sector result.
  - Source: `import json | from pathlib import Path |  | DATA_DIR = Path("data") | with open(DATA_DIR / "regions.geojson") as f: |     regions_fc = json.load(f) |  | def which_sector(lon, lat): |     # Use find_containing_feature, return sector name or "none" |     pass  # your code here |  | cities = [ |     ("Tehran",  51.388,  35.695), |     ("Riyadh",  46.675,  24.688), |     ("Cairo",   31.235,  30.044), |     ("Madrid",  -3.703,  40.417), |     ("Muscat",  58.593,  23.614), | ] |  | # Print: city name, lon, lat, which_sector result | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  Create **three overlapping blast zones** (800 km each) around Tehran, Riyadh, and Cairo.  1. Build them as a FeatureCollection using `make_circle`. 2. Use `find_all_containing_features` to test which zones contain each of these points:    - `(40.0, 30.0)` — Red Sea area    - `(50.0, 25.0)` — Gulf of Oman    - `(20.0, 28.0)` — Sudan 3. For each test point, print how many zones it falls in and which ones.
  - Source: `import math |  | # make_circle(lon, lat, radius_km) — defined in teaching cells above |  | # 1. Three 800 km blast zones: Tehran, Riyadh, Cairo | # 2. find_all_containing_features for each test point | # 3. Print zone membership for each point | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\05_Region_Classification.ipynb

- Cell 12
  - Prompt: ## Exercise A  Connect `classify_point` to a click handler.  1. Create a map showing all five sectors. 2. When the user clicks anywhere on the map, print the classification result:    - If inside a sector: print the sector name and description.    - If outside all sectors: print `"Outside all sectors"`. 3. Include the click coordinates (lat, lon) in the output.
  - Source: `from ipyleaflet import Map, GeoJSON, basemaps | from ipywidgets import Output | import json | from pathlib import Path |  | DATA_DIR = Path("data") | with open(DATA_DIR / "regions.geojson") as f: |     regions_fc = json.load(f) |  | out = Output() |  | # Map + click handler | # On click: extract lat/lon, flip to lon/lat, classify_point, print result | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  Handle the "outside all sectors" case gracefully in a pipeline.  Write a function `safe_classify(lon, lat)` that: 1. Returns a dict with `name`, `description`, and `status` keys. 2. If inside a sector: `status = "classified"`, `name` and `description` filled from properties. 3. If outside: `status = "unclassified"`, `name = "Unknown"`, `description = "Outside operational sectors"`. 4. Test it on at least 3 cities inside sectors and 2 outside.
  - Source: `def safe_classify(lon, lat): |     # Returns {name, description, status} |     # status: "classified" or "unclassified" |     pass  # your code here |  | test_locs = [ |     ("Tehran",   51.388,  35.695), |     ("Riyadh",   46.675,  24.688), |     ("Baghdad",  44.361,  33.338), |     ("Madrid",   -3.703,  40.417), |     ("Honolulu", -157.855, 21.305), | ] |  | for name, lon, lat in test_locs: |     result = safe_classify(lon, lat) |     print(f"{name}: status={result['status']}, sector={result['name']}")`


### Assignments\02-Missile_Geometry_202\_micro_lessons\11-Point_In_Polygon\06_Interactive_Click_Applications.ipynb

- Cell 11
  - Prompt: ## Exercise A  Build a **region classifier map** that:  1. Shows all five sectors. 2. On each click, prints the sector name and description in the output. 3. Places a Marker at the click location with a different color depending on whether the click was inside or outside a sector. 4. Accumulates all clicks — does not clear previous markers.
  - Source: `from ipyleaflet import Map, GeoJSON, Marker, basemaps | from ipywidgets import Output | import json | from pathlib import Path |  | DATA_DIR = Path("data") | with open(DATA_DIR / "regions.geojson") as f: |     regions_fc = json.load(f) |  | out = Output() |  | # Map showing all sectors | # Click handler: classify, print result, add persistent marker | # Inside click: one marker color; outside click: different color | # Your code here`

- Cell 13
  - Prompt: ## Exercise B  Build a **blast zone query map** that answers: *"Which targets can reach this location?"*  1. Draw three concentric rings (200 km, 500 km, 1000 km) around **Tehran** and **Riyadh** — six rings total. 2. On each click, determine which rings contain the click point using `point_in_ring`. 3. Print a summary: for each target, report the closest ring that contains the click (or "out of range"). 4. Example output:    ```    Click at lat=28.5  lon=50.0    Tehran:  within 500 km zone (432 km away)    Riyadh:  within 200 km zone (187 km away)    ```
  - Source: `from ipyleaflet import Map, GeoJSON, LayersControl, basemaps | from ipywidgets import Output | import math |  | # Target coordinates | tehran = (51.388, 35.695) | riyadh = (46.675, 24.688) |  | # 1. Three concentric rings per target (200, 500, 1000 km) | # 2. Click handler: determine which rings contain the click | # 3. For each target: report closest containing ring, distance | # 4. Display on map with LayersControl | # Your code here`


### Assignments\02-Missile_Geometry_202\_micro_lessons\12-Refactoring\01-From-Notebook-to-Module.ipynb

- Cell 24
  - Prompt: --- ## 8 — Refactoring Exercise  Below is a copy of `point_in_ring` from Module 11.  It uses `[lon, lat]` lists.
  - Source: `# YOUR TURN | # Refactor point_in_ring so that: | #   1. The point is a LatLon object (not separate lon, lat args) | #   2. The ring is a list of LatLon objects (not [lon,lat] lists) | #   3. The function still returns the correct True/False answers above |  | def point_in_ring_v2(point: LatLon, ring: list) -> bool: |     # Your code here |     ... |  |  | # Test — build the same ring using LatLon objects | ring_v2 = [ |     LatLon(lat=35, lon=-100), |     LatLon(lat=40, lon=-100), |     LatLon(lat=40, lon=-95), |     LatLon(lat=35, lon=-95), | ] | # Uncomment to test once implemented: | # print(point_in_ring_v2(LatLon(37.5, -97.0), ring_v2))   # True | # print(point_in_ring_v2(LatLon(37.5, -110.0), ring_v2))  # False`


## Assignments\03-Data_Manager


### Assignments\03-Data_Manager\_micro_lessons\00-Data_Exploration\00-Loading_and_Inspecting.ipynb

- Cell 17
  - Prompt: ## Exercise A  Print a **sorted list of unique values** for the `category` property across all features.  How many distinct categories exist?
  - Source: `# Print a sorted list of unique 'category' values across all features | # Your code here`

- Cell 19
  - Prompt: ## Exercise B  The `scalerank` property is an integer indicating importance — **lower values = more important** features.  Count how many features exist at each `scalerank` value. Print the results sorted by scalerank.
  - Source: `# Count features at each scalerank value | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\00-Data_Exploration\01-Measuring_the_Problem.ipynb

- Cell 18
  - Prompt: ## Exercise A  Find the **10 features with the most coordinate points**. For each, print the feature index (its position in the features list) and its coordinate count.  Which feature has the most points? What are its properties?
  - Source: `# Find the 10 features with the most coordinate points | # Print index and coordinate count for each | # Your code here`

- Cell 20
  - Prompt: ## Exercise B  The `scalerank` property controls at what zoom level a feature should appear. Features with `scalerank <= 3` are the most important — major trunk lines.  1. Count how many features have `scalerank <= 3` 2. Sum their coordinate points 3. What percentage of total coordinates do these "important" features account for?
  - Source: `# Count high-importance features (scalerank <= 3) and their coordinate share | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\01-Douglas_Peucker\00-The_Algorithm.ipynb

- Cell 14
  - Prompt: ## Exercise A  Consider this 5-point line:  ``` A = (0, 0) 1 = (1, 0.05) 2 = (2, 0.8) 3 = (3, 0.04) B = (4, 0) ```  Trace through the algorithm **by hand** (or in a comment) with `epsilon = 0.1`.  Which points are kept? Which are discarded? Show your reasoning for each step.
  - Source: `# Trace through Douglas-Peucker on the 5-point line with epsilon=0.1 | # Write your reasoning as comments, then plot the original and simplified result |  | five_points = [(0,0), (1, 0.05), (2, 0.8), (3, 0.04), (4, 0)] |  | # Round 1: reference line A→B is y=0, so distances are just y values | # ... |  | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Using the same 5-point line from Exercise A, trace the algorithm again with `epsilon = 1.0`.  How does the output change? What does this tell you about the relationship between epsilon and output size?
  - Source: `# Trace Douglas-Peucker on the same 5-point line with epsilon=1.0 | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\01-Douglas_Peucker\01-Implementation.ipynb

- Cell 16
  - Prompt: ## Exercise A  Add a print statement inside `douglas_peucker` that outputs a message each time it recurses. Run it on the 7-point example with `epsilon=0.3`.  How many recursive calls are made? Does the count match what you traced by hand in the previous notebook?
  - Source: `# Copy douglas_peucker here and add a print statement to count recursive calls | # Your code here |  | `

- Cell 18
  - Prompt: ## Exercise B  The current implementation works on `(x, y)` tuples. GeoJSON coordinates are stored as `[lon, lat]` lists.  Modify `douglas_peucker` (or write a wrapper) so it accepts GeoJSON-style `[lon, lat]` lists and returns the same format. Test it on a short hand-written list of coordinates.
  - Source: `# Adapt douglas_peucker to accept and return [lon, lat] lists | # Test with a short example | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\01-Douglas_Peucker\02-Epsilon_and_Tradeoffs.ipynb

- Cell 17
  - Prompt: ## Exercise A  Using your measured results from the table above, design the four LOD levels for the railroad project.  Fill in this table with the epsilon you would choose for each level and justify your choices:  | Level | Zoom Range | Epsilon | Reasoning | |-------|-----------|---------|------------| | Coarse | 1–3 | ? | | | Medium | 4–6 | ? | | | Fine | 7–10 | ? | | | Extra Fine | 11+ | ? | |  There is no single correct answer — defend your tradeoffs.
  - Source: `# Write your epsilon choices and reasoning as comments | # Your code here |  | coarse = 1.0 | medium = 0.5 | fine = 0.3 | extra = .03 | table=f""" | | Level | Zoom Range | Epsilon | Reasoning | | |-------|-----------|---------|------------| | | Coarse | 1–3 | {coarse} | | | | Medium | 4–6 | {medium} | | | | Fine | 7–10 | {fine} | | | | Extra Fine | 11+ | {extra} | | | """ |  | print(f"{'Level':<12} {'Zoom Range':>8} {'Epsilon':>8} {'Reasoning':>9}") | print("-" * 52) |  | c="Coarse" | z="1-3" | r="" | print(f"{c:<12} {z:>8} {coarse:>8} {r:>9}") | `

- Cell 19
  - Prompt: ## Exercise B  After simplification with `epsilon=1.0`, some features are reduced to exactly **2 points** — just a start and an end.  1. Count how many features in the full dataset are reduced to 2 points at epsilon=1.0. 2. Should we keep those 2-point features in a coarse LOD file, or discard them? Argue for one side.
  - Source: `# Count features reduced to 2 points at epsilon=1.0 | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\02-LOD_Generation\00-Designing_the_Pipeline.ipynb

- Cell 10
  - Prompt: ## Exercise A  Look at the collapse numbers from the table above. At `epsilon=1.0`, what fraction of the original 25,000+ features survive?  Now reconsider: should the coarse LOD also apply a `scalerank` filter, or is geometry simplification alone enough to reduce data volume to a usable level? Write your argument in a comment.
  - Source: `# Write your argument as comments | # Consider: what is the goal of the coarse level — correctness or speed? | # Your code here`

- Cell 12
  - Prompt: ## Exercise B  The `natlscale` property stores the intended display scale for each feature (e.g. `250` = designed for 1:250,000 maps).  Could `natlscale` be used as a LOD filter instead of `scalerank`? Write code that shows the distribution of `natlscale` values, then make a case for or against using it.
  - Source: `# Show distribution of natlscale values | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\02-LOD_Generation\01-Writing_the_LOD_Files.ipynb

- Cell 12
  - Prompt: ## Exercise A  The coarse level applies a `scalerank <= 4` filter before simplification. Modify the pipeline (in a copy below) to run the coarse level **without** the scalerank filter.  Compare: - How many features does the unfiltered coarse level contain? - How much larger is the file? - Is the scalerank filter worth keeping, or is geometry simplification alone sufficient?  Write your conclusion as a comment.
  - Source: `# Run coarse simplification without the scalerank filter | # Compare against the filtered version | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  The pipeline writes GeoJSON using `json.dump()`, which produces unformatted output (no indentation). This is intentional — indentation adds whitespace that inflates file size.  1. Write one of the LOD files again with `indent=2` to make it human-readable. 2. Compare the file size before and after. 3. By what percentage does indentation increase file size?  Do not keep the indented file — overwrite it with the compact version when you are done.
  - Source: `# Write a LOD file with indent=2, measure the size difference, then restore compact version | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\02-LOD_Generation\02-Comparing_the_Levels.ipynb

- Cell 12
  - Prompt: ## Exercise A  Pick one specific railroad feature that appears in all four LOD files — use the `rwdb_rr_id` property to find the same feature across files.  Plot that single feature at all four simplification levels on one chart. Label each with its point count.
  - Source: `# Find a feature by rwdb_rr_id that exists in all four LOD levels | # Plot it at all four simplification levels | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  Calculate the **compression ratio** for each LOD level — the ratio of original coordinate count to simplified coordinate count for the features they share.  Then answer: which level gives the best size reduction per unit of visual quality loss?
  - Source: `# Calculate compression ratio per LOD level | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\03-Bounding_Box_Culling\00-Bounding_Boxes.ipynb

- Cell 13
  - Prompt: ## Exercise A  Write a function `collection_bbox(features)` that returns the bounding box of an **entire FeatureCollection** — the smallest rectangle that contains all features.  Apply it to each of the four LOD files and compare the results. Do they all cover the same geographic extent?
  - Source: `# Write collection_bbox(features) and apply to all four LOD files | # Your code here`

- Cell 15
  - Prompt: ## Exercise B  Find the **5 features with the largest bounding box area** in the fine LOD file.  Bounding box area = `(lon_max - lon_min) * (lat_max - lat_min)`.  Print each one's bbox area and its `category` property. Do the results make geographic sense?
  - Source: `# Find the 5 features with the largest bounding box area in railroads_fine.geojson | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\03-Bounding_Box_Culling\01-Intersection_Test.ipynb

- Cell 11
  - Prompt: ## Exercise A  The current `bbox_intersects` function uses strict `<` and `>` comparisons — boxes that share only an edge (touching but not overlapping) return `True`.  Write a version `bbox_intersects_strict` that returns `False` for boxes that only touch at an edge or corner — they must have a non-zero overlap area to return `True`.  For a map renderer, which version is more appropriate? Why?
  - Source: `# Write bbox_intersects_strict and test it on the touching-edge cases | # Your code here`

- Cell 13
  - Prompt: ## Exercise B  Write a function `cull(features, viewport_bbox)` that takes a list of GeoJSON features and a viewport bounding box, and returns only the features that pass the intersection test.  Test it on the fine LOD file with the viewport set to Western Europe `[-10, 35, 30, 60]`. How many features survive?
  - Source: `import json | from pathlib import Path |  | # Write cull(features, viewport_bbox) and apply to the fine LOD file | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\03-Bounding_Box_Culling\02-Viewport_Culling.ipynb

- Cell 13
  - Prompt: ## Exercise A  The current map always uses the `fine` LOD file regardless of zoom. Modify the map so it uses `railroads_coarse.geojson` when zoom < 4 and `railroads_fine.geojson` when zoom >= 4.  This is a preview of Module 05 — just get it working here as a one-off.
  - Source: `# Load both LOD files and switch between them based on zoom level | # Your code here`

- Cell 15
  - Prompt: ## Exercise B  The culling function runs a **linear scan** — it checks every feature in order. For the fine LOD with ~20,000 features, measure how long a single cull call takes using `time.perf_counter()`.  Then calculate: if the user pans 10 times per second, how much CPU time does culling consume per second? Is this a problem?
  - Source: `import time |  | # Time a single cull() call on the fine LOD | # Calculate CPU cost at 10 pans/second | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\04-Spatial_Grid_Index\00-The_Grid_Idea.ipynb

- Cell 10
  - Prompt: ## Exercise A  Modify `cells_for_bbox` to work with a cell size of `5.0` instead of `10.0`. Then rerun the viewport table above.  How does the number of cells hit change? Does a smaller cell size always help query speed? Explain.
  - Source: `# Rerun the viewport table with cell_size=5.0 | # Your code here`

- Cell 12
  - Prompt: ## Exercise B  A feature with a very large bounding box — one that spans many degrees — will be assigned to many cells.  Load the fine LOD file, compute `cells_for_bbox` for every feature with a 10° grid, and find: 1. The feature assigned to the **most cells**. How many cells does it occupy? 2. The **average number of cells** per feature.
  - Source: `import json | from pathlib import Path |  | def feature_bbox(feature): |     coords = feature["geometry"]["coordinates"] |     lons = [c[0] for c in coords] |     lats = [c[1] for c in coords] |     return [min(lons), min(lats), max(lons), max(lats)] |  | with open(Path("../../data/lod/railroads_fine.geojson")) as f: |     fine = json.load(f) |  | # Find the feature assigned to the most cells | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\04-Spatial_Grid_Index\01-Building_the_Index.ipynb

- Cell 14
  - Prompt: ## Exercise A  Build the index with three different cell sizes: `5.0`, `10.0`, and `20.0` degrees.  For each, print: - Number of occupied cells - Total references (feature × cell assignments) - Build time  Which cell size uses the most memory? Which takes the longest to build?
  - Source: `# Build GridIndex at three different cell sizes and compare | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Find the **busiest cell** (the cell with the most feature references) in the 10° grid.   1. What geographic region does it cover? 2. Display just the features in that cell on a map. 3. Does the visual density match your expectation given the cell's location?
  - Source: `# Find the busiest cell, identify its geographic region, and display its features | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\04-Spatial_Grid_Index\02-Querying_and_Benchmarking.ipynb

- Cell 14
  - Prompt: ## Exercise A  The benchmark shows the grid is slower than linear scan at world zoom. Explain **why** — trace through what the grid query does when `viewport_bbox` covers all 648 cells, and compare the work to a plain list comprehension.
  - Source: `# Write your explanation as comments | # Optionally instrument the query to count operations | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Try Shapely's `STRtree` as an alternative index. Build it from the fine LOD features and time it against the same five viewports.  ```python from shapely.strtree import STRtree from shapely.geometry import box ```  Compare the STRtree query times to your grid index. Where does the R-tree win?
  - Source: `# Build a Shapely STRtree from the fine LOD features | # Benchmark against the same viewports used above | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\05-Zoom_Layer_Switching\00-The_Decision_Function.ipynb

- Cell 12
  - Prompt: ## Exercise A  The transition thresholds in `get_lod_with_hysteresis` are hardcoded. Refactor it to accept a `thresholds` parameter — a dict that specifies upgrade and downgrade zoom values for each transition.  This makes the function reusable without editing its body.
  - Source: `# Refactor get_lod_with_hysteresis to accept a thresholds parameter | # Example structure: | # thresholds = { | #     "coarse":     {"up_at": 4}, | #     "medium":     {"up_at": 7,  "down_at": 2}, | #     "fine":       {"up_at": 11, "down_at": 5}, | #     "extra_fine": {             "down_at": 9}, | # } | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  Visualize the hysteresis. Plot two lines on the same chart:  1. The LOD level when zooming **in** from zoom 0 to 14 (encoded as 0=coarse, 1=medium, 2=fine, 3=extra_fine) 2. The LOD level when zooming **out** from zoom 14 to 0  The two lines should diverge at the transition zones — that gap is the hysteresis band.
  - Source: `# Plot zoom-in vs zoom-out LOD trajectories to show the hysteresis band | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\05-Zoom_Layer_Switching\01-Live_Layer_Switching.ipynb

- Cell 12
  - Prompt: ## Exercise A  Add a **zoom indicator** to the status bar that shows the current zoom level and a simple text label of the geographic scale (e.g. `zoom 5 — country scale`).  Use the zoom-to-scale table from Notebook 00 as a guide.
  - Source: `# Copy the map setup from above and add a zoom level + scale label to the status bar | # Your code here`

- Cell 14
  - Prompt: ## Exercise B  The `update()` function is called for both zoom and bounds changes — a single event handler covers both.  This means if the user zooms AND pans at the same time (which ipyleaflet reports as two rapid events), `update()` runs twice. The second call sees the final state and overwrites the first — so the result is correct, but redundant work was done.  Add a `print` statement inside `update()` that shows which property triggered the call (`zoom` or `bounds`). Then scroll/zoom the map and observe the sequence. Do zoom and bounds always fire together?
  - Source: `# Copy the map and add print(change['name']) inside update() to trace events | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\06-Putting_It_Together\00-The_Viewer.ipynb

- Cell 14
  - Prompt: ## Exercise A  Add a second style dimension: color the lines by `category` property.  1. Find the unique `category` values in the fine LOD file 2. Assign a distinct color to each 3. Update `style_callback` to use category color + scalerank weight together  The result should show the railroad network colored by line type.
  - Source: `# Add category-based coloring to style_callback | # Your code here`

- Cell 16
  - Prompt: ## Exercise B  Add a tooltip: when the user hovers over a railroad feature, show its `category` and `scalerank` in a widget below the map.  Hint: use the GeoJSON layer's `on_hover` event.
  - Source: `# Add hover tooltip showing category and scalerank | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\06-Putting_It_Together\01-What_We_Built.ipynb

- Cell 13
  - Prompt: ## Exercise A  Measure the peak memory usage of the viewer at startup (after all 4 LOD files are loaded and all 4 indexes are built).  Use Python's `tracemalloc` module:  ```python import tracemalloc tracemalloc.start() # ... load and build ... current, peak = tracemalloc.get_traced_memory() print(f"Peak memory: {peak / 1_000_000:.1f} MB") ```  How does this compare to just reading the four files without building indexes?
  - Source: `# Measure peak memory: (a) loading files only, (b) loading + building indexes | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\07-The_Library_Version\00-What_Are_Vector_Tiles.ipynb

- Cell 8
  - Prompt: ## Exercise A  At zoom 12, the world is divided into `2^12 × 2^12 = 4096 × 4096 = ~16.7 million` tiles.  1. How many tiles cover Western Europe at zoom 12? (Approximate using the bounding box [-10, 35, 30, 60]) 2. If each tile is 100 KB on average, how much data would the user need to download to view all of Western Europe at zoom 12?  Compare that to loading our `extra_fine` GeoJSON for the same region.
  - Source: `# Calculate tile count for Western Europe at zoom 12 | # Estimate download size vs. GeoJSON approach | # Your code here`


### Assignments\03-Data_Manager\_micro_lessons\07-The_Library_Version\01-Using_Tippecanoe.ipynb

- Cell 13
  - Prompt: ## Exercise A  Run `tippecanoe` a second time with `--maximum-zoom=8` and compare the output file size.  Then answer: what did limiting the maximum zoom cost us in terms of user experience, and what did it save?
  - Source: `# Run tippecanoe with --maximum-zoom=8 and compare output size | # Your code here`

- Cell 15
  - Prompt: ## Exercise B  The `--simplification=10` flag sets the tolerance in **tile pixels**, not degrees. At zoom 14, a tile covers roughly 2.4km × 2.4km in 4096 pixels — so one pixel ≈ 0.6m.  Calculate what `--simplification=10` means in meters at zoom levels 2, 5, 8, and 12. Compare these to the degree-based epsilon values we chose in Module 02.
  - Source: `# Calculate simplification tolerance in meters at different zoom levels | # Compare to our Module 02 epsilon choices | # Your code here`
