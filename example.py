# geojson_shapely_example.py
#
# This script demonstrates the combined use of the geojson and shapely libraries.
#
# To run this code, you need to install the necessary libraries:
# pip install shapely
# pip install geojson

import geojson
from shapely.geometry import shape, Point
from shapely.ops import transform
import pyproj

def main():
    """
    Main function to demonstrate GeoJSON and Shapely operations.
    """
    print("--- GeoJSON and Shapely Demonstration ---")

    # 1. Define a geographical feature using GeoJSON format.
    # This polygon roughly represents Yamashita Park in Yokohama, Japan.
    # GeoJSON uses (longitude, latitude) order.
    park_geojson = {
        "type": "Polygon",
        "coordinates": [[
            [139.6485, 35.4460],
            [139.6530, 35.4485],
            [139.6520, 35.4495],
            [139.6475, 35.4470],
            [139.6485, 35.4460]
        ]]
    }

    # Define two points of interest in GeoJSON format.
    # Hikawa Maru is inside Yamashita Park.
    point_inside_geojson = {
        "type": "Point",
        "coordinates": [139.6500, 35.4475]
    }
    # Yokohama Landmark Tower is outside the park.
    point_outside_geojson = {
        "type": "Point",
        "coordinates": [139.6305, 35.4556]
    }

    print("\nStep 1: Defined GeoJSON for a park and two points.")
    print("Park Polygon:", park_geojson)
    print("Inside Point:", point_inside_geojson)
    print("Outside Point:", point_outside_geojson)

    # 2. Convert GeoJSON dictionaries into Shapely objects.
    # The `shape()` function from shapely is perfect for this.
    park_shape = shape(park_geojson)
    point_inside_shape = shape(point_inside_geojson)
    point_outside_shape = shape(point_outside_geojson)

    print("\nStep 2: Converted GeoJSON dictionaries into Shapely objects.")
    print("Shapely Park Object Type:", type(park_shape))
    print("Shapely Point Object Type:", type(point_inside_shape))


    # 3. Perform spatial analysis using Shapely methods.
    # Let's check if the points are within the park's boundaries.
    is_inside = park_shape.contains(point_inside_shape)
    is_outside = park_shape.contains(point_outside_shape)

    print("\nStep 3: Performing spatial analysis.")
    print(f"Is the Hikawa Maru point inside the park? -> {is_inside}")
    print(f"Is the Landmark Tower point inside the park? -> {not is_outside}")


    # 4. Create a new geometry using a Shapely operation.
    # Let's create a 100-meter buffer zone around the 'inside' point.
    #
    # WARNING: Shapely's buffer operation works in Cartesian coordinates, not
    # degrees. A buffer of 0.001 degrees is not constant in meters.
    # To do this accurately, we must project from geographic coordinates (WGS84)
    # to a projected coordinate system (like UTM).

    # Define the transformation from WGS84 (lat/lon) to UTM zone 54N (meters)
    # and back.
    project_to_meters = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32654", always_xy=True).transform
    project_to_degrees = pyproj.Transformer.from_crs("EPSG:32654", "EPSG:4326", always_xy=True).transform

    # Project the point to meters
    point_in_meters = transform(project_to_meters, point_inside_shape)

    # Create a 100-meter buffer
    buffer_in_meters = point_in_meters.buffer(100)

    # Project the buffer back to degrees (lat/lon)
    buffer_in_degrees = transform(project_to_degrees, buffer_in_meters)

    print("\nStep 4: Created a 100-meter buffer around the inside point.")
    print("The buffer operation was performed in a meter-based coordinate system for accuracy.")


    # 5. Convert the resulting Shapely object back to a GeoJSON Feature.
    # We can use the `geojson` library to structure it nicely as a Feature
    # with properties.
    buffer_feature = geojson.Feature(
        geometry=buffer_in_degrees,
        properties={"name": "100m Safety Zone around Hikawa Maru"}
    )

    print("\nStep 5: Converted the buffer Shapely object back to a GeoJSON Feature.")

    # `dumps` from the geojson library creates a nicely formatted string.
    buffer_geojson_str = geojson.dumps(buffer_feature, indent=4)

    print("\n--- Generated Buffer GeoJSON ---")
    print(buffer_geojson_str)
    print("\n--- End of Demonstration ---")


if __name__ == '__main__':
    main()


