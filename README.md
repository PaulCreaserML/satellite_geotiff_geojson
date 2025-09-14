# GeoJSON and Shapely Demonstration
This Python script provides a practical example of how to use the geojson, shapely, and pyproj libraries for common geospatial operations. It demonstrates the full workflow from defining geographic data in GeoJSON format, performing spatial analysis and transformations with Shapely, to converting the results back into GeoJSON.

The example is based on real-world coordinates from Yokohama, Japan.

📍 Core Concepts Demonstrated
This script walks through the following key geospatial tasks:

Data Definition: Creating Point and Polygon geometries using the standard GeoJSON dictionary format.

GeoJSON to Shapely Conversion: Parsing GeoJSON data into shapely geometric objects to prepare for analysis.

Spatial Analysis: Using Shapely's methods to perform a "point in polygon" test (specifically, polygon.contains(point)).

Coordinate Reference System (CRS) Transformation: Using pyproj to project coordinates from a geographic system (WGS84, degrees) to a projected system (UTM, meters) to perform accurate distance-based calculations.

Geometric Operations: Creating a 100-meter buffer around a point using Shapely's .buffer() method.

Shapely to GeoJSON Conversion: Converting the resulting Shapely geometry back into a structured GeoJSON Feature object, complete with properties.

# Requirements
To run this script, you will need Python 3 and the following libraries:

## geojson
## shapely
## pyproj

You can install all the required libraries using pip:

pip install geojson shapely pyproj

#  How to Run
Once the dependencies are installed, you can run the script directly from your terminal:

python example.py

# Expected Output
Running the script will print a step-by-step log of its operations to the console, culminating in the final GeoJSON output for the calculated buffer zone.

--- GeoJSON and Shapely Demonstration ---

Step 1: Defined GeoJSON for a park and two points.
Park Polygon: {'type': 'Polygon', 'coordinates': [[[139.6485, 35.446], [139.653, 35.4485], [139.652, 35.4495], [139.6475, 35.447], [139.6485, 35.446]]]}
Inside Point: {'type': 'Point', 'coordinates': [139.65, 35.4475]}
Outside Point: {'type': 'Point', 'coordinates': [139.6305, 35.4556]}

Step 2: Converted GeoJSON dictionaries into Shapely objects.
Shapely Park Object Type: <class 'shapely.geometry.polygon.Polygon'>
Shapely Point Object Type: <class 'shapely.geometry.point.Point'>

Step 3: Performing spatial analysis.
Is the Hikawa Maru point inside the park? -> True
Is the Landmark Tower point inside the park? -> True

Step 4: Created a 100-meter buffer around the inside point.
The buffer operation was performed in a meter-based coordinate system for accuracy.

Step 5: Converted the buffer Shapely object back to a GeoJSON Feature.

--- Generated Buffer GeoJSON ---
{
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [139.651117..., 35.4475...],
                [139.651108..., 35.4475...],
                ...
                [139.651117..., 35.4475...]
            ]
        ]
    },
    "properties": {
        "name": "100m Safety Zone around Hikawa Maru"
    }
}
--- End of Demonstration ---

(Note: The full list of coordinates for the buffer polygon has been truncated for brevity.)

# Data display

1. Online Tools (The Quickest Way)

For a fast and easy visualization, web-based tools are your best bet.

geojson.io: This is the most popular tool for this purpose. It's a free, interactive editor and viewer right in your browser.

Run your Python script: python example.py.

Copy the entire GeoJSON Feature object that is printed to your console.

Go to geojson.io.

Delete the sample text in the editor on the right and paste your copied GeoJSON.

You will immediately see the buffer polygon rendered on the map.
