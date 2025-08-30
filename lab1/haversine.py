"""Haversine distance between two GeoJSON points from ``points.json``.

This script reads the file ``points.json`` located in the same directory,
expects a GeoJSON FeatureCollection with exactly two Point features, and
prints their great-circle distance in meters using the Haversine formula.
"""

import json
import sys
from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class Geometry:
    """Geometry for a GeoJSON Point."""
    type: str
    coordinates: Tuple[float, float]  # (lon, lat)

@dataclass
class Feature:
    """GeoJSON Feature holding a Point geometry."""
    id: int
    type: str
    properties: Dict[str, str]
    geometry: Geometry

@dataclass
class Points:
    """GeoJSON FeatureCollection of two points."""
    type: str
    features: List[Feature]


def geometry_from_dict(d: Dict) -> Geometry:
    """Convert a dictionary to a Geometry object."""
    coords = d["coordinates"]
    lon = float(coords[0])
    lat = float(coords[1])
    return Geometry(type=d["type"], coordinates=(lon, lat))


def feature_from_dict(d: Dict) -> Feature:
    """Convert a dictionary to a Feature object."""
    return Feature(
        id=int(d["id"]),
        type=d["type"],
        properties=dict(d["properties"]),
        geometry=geometry_from_dict(d["geometry"]),
    )


def points_from_dict(d: Dict) -> Points:
    """Convert a dictionary to a Points object."""
    return Points(
        type=d["type"],
        features=[feature_from_dict(f) for f in d["features"]],
    )



geojson_path = Path(__file__).resolve().parent / "points.json"
try:
    with open(geojson_path, "r", encoding="utf-8") as f:
        raw: Dict = json.load(f)
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

points: Points = points_from_dict(raw)
feature1, feature2 = points.features[0], points.features[1]

# GeoJSON coordinates are stored as (longitude, latitude)
lon1, lat1 = feature1.geometry.coordinates
lon2, lat2 = feature2.geometry.coordinates

earth_radius = 6371000  # meter
phi1 = radians(lat1)
lam1 = radians(lon1)
phi2 = radians(lat2)
lam2 = radians(lon2)

a = sin((phi2 - phi1) / 2) ** 2 + cos(phi1) * cos(phi2) * sin((lam2 - lam1) / 2) ** 2
result = 2 * earth_radius * asin(sqrt(a))
print(result)
