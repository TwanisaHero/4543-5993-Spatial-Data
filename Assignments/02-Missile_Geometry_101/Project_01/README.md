# Project 01: Missile Geometry 101

Completed reference deliverable.

## Files

- `Project_01_Analysis.ipynb` - full analysis notebook
- `project_01_threat_map.html` - generated interactive map
- `project_01_analysis.csv` - intersection and damage-zone table
- `project_01_threats.csv` - simulated threat input table

## Summary

The notebook simulates 12 incoming threats around a fixed Wichita Falls base, computes distance to base, generates trajectory lines, checks country intersections, creates endpoint damage buffers, and saves a Folium map. The map includes world boundaries, base location, threat origins, trajectories, semi-transparent damage buffers, layer control, and a legend.

## Notes

The damage buffers use an approximate kilometer-to-degree conversion. That is acceptable for a learning reference, but a serious spatial analysis should use projected or geodesic buffering.
