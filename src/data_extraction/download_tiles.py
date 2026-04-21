import requests
import os


def download_xyz_tiles(bbox, zoom):
    """Download thermal map tiles from an XYZ tile server.

    This function will download raster tiles covering the given bounding box
    at the specified zoom level and save them locally.

    Args:
        bbox (tuple): Bounding box as (min_lon, min_lat, max_lon, max_lat).
        zoom (int): Zoom level for the tiles to download.

    Returns:
        list[str]: Paths to the downloaded tile files.
    """
    pass
