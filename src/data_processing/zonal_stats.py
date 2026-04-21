import geopandas as gpd
import rasterio


def calculate_thermal_index(polygon, raster):
    """Calculate the thermal index for a given polygon from a raster dataset.

    This function will extract and aggregate raster pixel values within the
    polygon boundary to produce a thermal index metric per spatial unit.

    Args:
        polygon (shapely.geometry.Polygon): The spatial boundary to analyse.
        raster (str or rasterio.DatasetReader): Path to or open raster dataset.

    Returns:
        float: The calculated thermal index value for the polygon.
    """
    pass
