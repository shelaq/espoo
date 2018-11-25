from django.contrib.gis.db import models

# Create your models here.

class BusStops(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    route = models.CharField('REITTI', max_length=100)
    name = models.CharField('NIMI', max_length=100)
    transport_type = models.IntegerField('VERKKO')
    tariff_area = models.CharField('TARIFFIALU', max_length=2)

    # GeoDjango-specific: a geometry field (PointField)
    mpoly = models.PointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class EspooSmallRegions(models.Model):
    kokotun = models.CharField(max_length=254)
    kunta = models.CharField(max_length=254)
    suur = models.CharField(max_length=254)
    tila = models.CharField(max_length=254)
    pien = models.CharField(max_length=254)
    nimi = models.CharField(max_length=254)
    nimi_iso = models.CharField(max_length=254)
    mtryhm = models.IntegerField()
    geom = models.MultiPolygonField(srid=4258)

class EspooRegionalData(models.Model):
    district_id = models.IntegerField()
    year = models.IntegerField()
    language_type = models.CharField(max_length=30)
    language_num_ppl_speak = models.IntegerField()

class EspooPopulations(models.Model):
    district_id = models.IntegerField()
    year = models.IntegerField()
    total_population = models.IntegerField(null=True)
    moved_to_municipality = models.IntegerField(null=True)
    sisainen_in_migration = models.IntegerField(null=True)
    moved_from_municipality = models.IntegerField(null=True)
    sisainen_out_migration = models.IntegerField(null=True)
    total_net_migration = models.IntegerField(null=True)
