import os
from django.contrib.gis.utils import LayerMapping
from .models import BusStops, EspooSmallRegions

# http://data-hslhrt.opendata.arcgis.com/datasets/c3a01a65b7a0467cba2a14935be8c2a2_0?geometry=23.952%2C60.098%2C25.687%2C60.302&uiTab=table
bus_stop_mapping = {
    'name' : 'NIMI',
    'route' : 'REITTI',
    'transport_type' : 'VERKKO',
    'tariff_area' : 'TARIFFIALU',
    'mpoly' : 'POINT',
}

# https://geoserver.hel.fi/geoserver/seutukartta/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=seutukartta:Espoo_pienalueet&maxFeatures=1000000&outputFormat=SHAPE-ZIP
espoosmallregions_mapping = {
    'kokotun': 'kokotun',
    'kunta': 'kunta',
    'suur': 'suur',
    'tila': 'tila',
    'pien': 'pien',
    'nimi': 'nimi',
    'nimi_iso': 'nimi_iso',
    'mtryhm': 'mtryhm',
    'geom': 'MULTIPOLYGON',
}

bus_stop_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'HSLn_pysäkit_linjoittain_syksy_2018.shp'),
)

espoo_region_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Espoo_pienalueetPolygon.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        EspooSmallRegions, espoo_region_shp, espoosmallregions_mapping,
        transform=True, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
